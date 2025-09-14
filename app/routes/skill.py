from flask import request, render_template,Blueprint, redirect, url_for, flash 
from app.models import User ,Skill, user_skills
from app.forms.skillforms import SkillForm
from flask_login import login_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db 
from sqlalchemy import insert , select , text
import pandas as pd

bp=Blueprint("skill", __name__)

@bp.route("/add_skill", methods=["GET", "POST"])
@login_required
def add_skill():
    form=SkillForm()
    if form.validate_on_submit():
        skill=Skill.query.filter_by(name=form.name.data).first()
        if not skill:
            skill=Skill(name=form.name.data.strip().lower())
            db.session.add(skill)
            db.session.commit()

        sql_stmt = text("SELECT * FROM user_skills WHERE user_id=:uid AND skill_id=:sid")

        # Execute query
        existing = db.session.execute(
            sql_stmt,
            {"uid": current_user.id, "sid": skill.id}
        ).fetchone()

        if existing:
             flash("You have already added this skill.", "warning")
        
        else:
            stmt = insert(user_skills).values(
                user_id=current_user.id,
                skill_id=skill.id,
                type=form.type.data.lower()
            )
            db.session.execute(stmt)
            db.session.commit()

            flash(f"Skill '{skill.name}' added as {form.type.data}!", "success")
        return redirect(url_for("skill.dashboard"))
    return render_template("add_skill.html", form=form)


@bp.route("/dashboard")
@login_required
def dashboard():
    # Get all skills + user associations from DB
    sql = """
    SELECT 
        u.id AS user_id,
        u.username, u.email,
        s.id AS skill_id, 
        s.name AS skill_name, 
        us.type
    FROM user_skills us
    JOIN "user" u ON u.id = us.user_id
    JOIN skill s ON s.id = us.skill_id
    """
    df = pd.read_sql(sql, db.engine)

    # Separate offered and requested
    offered = df[df["type"] == "offered"]
    requested = df[df["type"] == "requested"]


    matches = []
    seen = set()

    # Loop through all rows
    for _, row1 in df.iterrows():
        for _, row2 in df.iterrows():
            # Skip same user
            if row1.user_id == row2.user_id:
                continue
            # Match offered -> requested or requested -> offered
            if row1.skill_name == row2.skill_name and row1.type != row2.type:
                key = tuple(sorted([row1.user_id, row2.user_id])) + (row1.skill_name,)
                if key not in seen:
                    if row1.type == "requested":
                        requester, provider = row1, row2
                    else:
                        requester, provider = row2, row1

                    matches.append({
                        "skill": row1.skill_name,
                        "requester": [requester.username, requester.email],
                        "provider": [provider.username, provider.email]
                    })
                    seen.add(key)

    user_skills = df[df["user_id"] == current_user.id]

    return render_template(
        "dashboard.html",
        user=current_user,
        user_skills=user_skills.to_dict(orient="records"),
        matches=matches
    )

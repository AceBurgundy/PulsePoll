from pandas import DataFrame, read_csv, Series, notnull
from Engine.text_processor import process_text
from Engine.models import Candidate, Comment
from Engine import create_app, db
from datetime import datetime
from Engine.emotion import *

app = create_app()
with app.app_context():

    dataset_path: str = "D:\Programming\Projects\Flask-Vanilla\AI-Presidential-Election-Sentiment-Analyzer\Engine\candidate\combined.csv"
    dataset: DataFrame = read_csv(dataset_path, encoding='latin')

    dataset["Translated"]: Series = dataset["Translated"].apply(process_text)

    for index, row in dataset.iterrows():

        candidate_name_dirty: str = row["Candidate"]
        candidate_name: str = candidate_name_dirty.strip()

        if not candidate_name:
            continue

        candidate: Candidate = Candidate.query.filter_by(name=candidate_name).first()

        if not candidate:
            image: str = candidate_name.replace(' ', '-') + '.webp'
            candidate: Candidate = Candidate(
                name=candidate_name,
                content="Candidate running for precidency in 2022",
                image=image
            )

            db.session.add(candidate)

        date_time_posted = None
        has_date: bool = notnull(row["Date"])
        has_time: bool = notnull(row["Time"])

        if has_date and has_time:
            date_str: str = f"{row['Date']} {row['Time']}".strip()
            date_time_posted: datetime = datetime.strptime(date_str, '%m/%d/%Y %I:%M %p')
        elif has_date:
            date_str: str = f"{row['Date']}"
            date_time_posted: datetime = datetime.strptime(date_str, '%m/%d/%Y')
        elif has_time:
            date_str: str = f"{row['Time']}"
            date_time_posted: datetime = datetime.strptime(date_str, '%I:%M %p')
        else:
            date_time_posted = None

        if "Comments" in row and row["Comments"]:
            text: str = row["Comments"]

            comment: Comment = Comment.query.filter_by(text=text).first()

            if comment:
                continue

            translated_comment: str = row["Translated"]
            emotion_label: str = get_emotion(translated_comment)
            username: str = row["User"]

            comment: Comment = Comment(
                text=text,
                date_time_posted=date_time_posted,
                username=username,
                emotion=emotion_label,
                candidate_id=candidate.id
            )

            db.session.add(comment)

    db.session.commit()
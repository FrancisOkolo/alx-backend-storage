#!/usr/bin/env python3
"""Python function that returns all students sorted by average
"""

def top_students(mongo_collection):
    """calculating average score of students
    """
    students = mongo_collection.aggregate([
            {
                "$project":
                    {
                        "name": "$name",
                        "averageScore": {"$avg": "$topics.score"},
                    },
            },
            {
                "$sort":
                    {
                        "averageScore": -1
                    },
            },
    ])
    return students

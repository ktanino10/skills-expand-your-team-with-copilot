"""
Mock database implementation for development without MongoDB
"""

from argon2 import PasswordHasher
from typing import Dict, Any, List, Optional
import copy

class MockCollection:
    """Mock MongoDB collection for development"""
    
    def __init__(self):
        self.data = {}
    
    def count_documents(self, query: dict) -> int:
        if not query:
            return len(self.data)
        return len([doc for doc in self.data.values() if self._matches_query(doc, query)])
    
    def find(self, query: dict = None) -> List[Dict[str, Any]]:
        if not query:
            return [{"_id": k, **v} for k, v in self.data.items()]
        
        results = []
        for k, v in self.data.items():
            doc = {"_id": k, **v}
            if self._matches_query(doc, query):
                results.append(doc)
        return results
    
    def find_one(self, query: dict) -> Optional[Dict[str, Any]]:
        if "_id" in query:
            doc_id = query["_id"]
            if doc_id in self.data:
                return {"_id": doc_id, **self.data[doc_id]}
        return None
    
    def insert_one(self, doc: Dict[str, Any]):
        doc_id = doc.pop("_id")
        self.data[doc_id] = copy.deepcopy(doc)
    
    def update_one(self, query: dict, update: dict):
        if "_id" in query:
            doc_id = query["_id"]
            if doc_id in self.data:
                if "$set" in update:
                    self.data[doc_id].update(update["$set"])
                elif "$push" in update:
                    for field, value in update["$push"].items():
                        if field not in self.data[doc_id]:
                            self.data[doc_id][field] = []
                        self.data[doc_id][field].append(value)
                elif "$pull" in update:
                    for field, value in update["$pull"].items():
                        if field in self.data[doc_id]:
                            if value in self.data[doc_id][field]:
                                self.data[doc_id][field].remove(value)
    
    def aggregate(self, pipeline: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # Simple implementation for specific aggregation patterns
        results = []
        for doc in self.data.values():
            for stage in pipeline:
                if "$unwind" in stage:
                    field = stage["$unwind"].replace("$", "")
                    if field in doc:
                        for item in doc[field]:
                            results.append({field.split(".")[-1]: item})
                elif "$group" in stage:
                    group_stage = stage["$group"]
                    if "_id" in group_stage:
                        field = group_stage["_id"].replace("$", "")
                        unique_values = set()
                        for result in results:
                            if field in result:
                                unique_values.add(result[field])
                        results = [{"_id": val} for val in unique_values]
                elif "$sort" in stage:
                    # Sort by _id field
                    results.sort(key=lambda x: x.get("_id", ""))
        return results
    
    def _matches_query(self, doc: Dict[str, Any], query: dict) -> bool:
        """Simple query matching logic"""
        for key, value in query.items():
            if "." in key:
                # Handle nested fields like "schedule_details.days"
                parts = key.split(".")
                current = doc
                for part in parts:
                    if part not in current:
                        return False
                    current = current[part]
                
                if isinstance(value, dict):
                    if "$in" in value:
                        # Check if any of the values in the array match
                        if not isinstance(current, list):
                            return False
                        if not any(item in value["$in"] for item in current):
                            return False
                    elif "$gte" in value:
                        if current < value["$gte"]:
                            return False
                    elif "$lte" in value:
                        if current > value["$lte"]:
                            return False
                else:
                    if current != value:
                        return False
            else:
                if isinstance(value, dict):
                    if "$exists" in value:
                        field_exists = key in doc
                        if value["$exists"] != field_exists:
                            return False
                    elif "$in" in value:
                        if key not in doc or doc[key] not in value["$in"]:
                            return False
                    elif "$gte" in value:
                        if key not in doc or doc[key] < value["$gte"]:
                            return False
                    elif "$lte" in value:
                        if key not in doc or doc[key] > value["$lte"]:
                            return False
                else:
                    if key not in doc or doc[key] != value:
                        return False
        return True

# Mock database instances
activities_collection = MockCollection()
teachers_collection = MockCollection()

# Methods
def hash_password(password):
    """Hash password using Argon2"""
    ph = PasswordHasher()
    return ph.hash(password)

def init_database():
    """Initialize database if empty"""
    # Initialize activities if empty
    if activities_collection.count_documents({}) == 0:
        for name, details in initial_activities.items():
            activities_collection.insert_one({"_id": name, **details})
            
    # Initialize teacher accounts if empty
    if teachers_collection.count_documents({}) == 0:
        for teacher in initial_teachers:
            teachers_collection.insert_one({"_id": teacher["username"], **teacher})

# Initial database if empty
initial_activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Mondays and Fridays, 3:15 PM - 4:45 PM",
        "schedule_details": {
            "days": ["Monday", "Friday"],
            "start_time": "15:15",
            "end_time": "16:45"
        },
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
        "difficulty": "Intermediate"
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 7:00 AM - 8:00 AM",
        "schedule_details": {
            "days": ["Tuesday", "Thursday"],
            "start_time": "07:00",
            "end_time": "08:00"
        },
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
        "difficulty": "Beginner"
    },
    "Morning Fitness": {
        "description": "Early morning physical training and exercises",
        "schedule": "Mondays, Wednesdays, Fridays, 6:30 AM - 7:45 AM",
        "schedule_details": {
            "days": ["Monday", "Wednesday", "Friday"],
            "start_time": "06:30",
            "end_time": "07:45"
        },
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:30 PM",
        "schedule_details": {
            "days": ["Tuesday", "Thursday"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and compete in basketball tournaments",
        "schedule": "Wednesdays and Fridays, 3:15 PM - 5:00 PM",
        "schedule_details": {
            "days": ["Wednesday", "Friday"],
            "start_time": "15:15",
            "end_time": "17:00"
        },
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various art techniques and create masterpieces",
        "schedule": "Thursdays, 3:15 PM - 5:00 PM",
        "schedule_details": {
            "days": ["Thursday"],
            "start_time": "15:15",
            "end_time": "17:00"
        },
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Study Group": {
        "description": "Collaborative study sessions for exam preparation",
        "schedule": "Mondays, 7:00 AM - 8:00 AM",
        "schedule_details": {
            "days": ["Monday"],
            "start_time": "07:00",
            "end_time": "08:00"
        },
        "max_participants": 8,
        "participants": ["sebastian@mergington.edu", "jackson@mergington.edu"]
    },
    "Math Competition": {
        "description": "Solve challenging problems and prepare for math competitions",
        "schedule": "Tuesdays, 7:15 AM - 8:00 AM",
        "schedule_details": {
            "days": ["Tuesday"],
            "start_time": "07:15",
            "end_time": "08:00"
        },
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"],
        "difficulty": "Advanced"
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 3:30 PM - 5:30 PM",
        "schedule_details": {
            "days": ["Friday"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "amelia@mergington.edu"],
        "difficulty": "Intermediate"
    },
    "Weekend Robotics Workshop": {
        "description": "Build and program robots in our state-of-the-art workshop",
        "schedule": "Saturdays, 10:00 AM - 2:00 PM",
        "schedule_details": {
            "days": ["Saturday"],
            "start_time": "10:00",
            "end_time": "14:00"
        },
        "max_participants": 15,
        "participants": ["ethan@mergington.edu", "oliver@mergington.edu"],
        "difficulty": "Advanced"
    },
    "Science Olympiad": {
        "description": "Weekend science competition preparation for regional and state events",
        "schedule": "Saturdays, 1:00 PM - 4:00 PM",
        "schedule_details": {
            "days": ["Saturday"],
            "start_time": "13:00",
            "end_time": "16:00"
        },
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "lucas@mergington.edu"],
        "difficulty": "Intermediate"
    },
    "Sunday Chess Tournament": {
        "description": "Weekly tournament for serious chess players with rankings",
        "schedule": "Sundays, 2:00 PM - 5:00 PM",
        "schedule_details": {
            "days": ["Sunday"],
            "start_time": "14:00",
            "end_time": "17:00"
        },
        "max_participants": 16,
        "participants": ["william@mergington.edu", "jacob@mergington.edu"],
        "difficulty": "Advanced"
    },
    "Manga Maniacs": {
        "description": "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
        "schedule": "Tuesdays, 7:00 PM - 8:00 PM",
        "schedule_details": {
            "days": ["Tuesday"],
            "start_time": "19:00",
            "end_time": "20:00"
        },
        "max_participants": 15,
        "participants": [],
        "difficulty": "Beginner"
    }
}

initial_teachers = [
    {
        "username": "mrodriguez",
        "display_name": "Ms. Rodriguez",
        "password": hash_password("art123"),
        "email": "mrodriguez@mergington.edu"
    },
    {
        "username": "mchen",
        "display_name": "Mr. Chen",
        "password": hash_password("chess456"),
        "email": "mchen@mergington.edu"
    }
]
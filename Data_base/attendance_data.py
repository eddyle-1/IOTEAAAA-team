import json
from datetime import datetime
import geopy.distance
from geopy.geocoders import Nominatim

class AttendanceRecord:
    def __init__(self, student_id, class_id, timestamp, latitude, longitude, status):
        self.student_id = student_id
        self.class_id = class_id
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        self.status = status  # "present" or "absent"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "class_id": self.class_id,
            "timestamp": self.timestamp,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "status": self.status
        }

class AttendanceManager:
    def __init__(self):
        self.attendance_file = 'attendance_records.json'
        self.class_locations = {
            "MATH101": {"latitude": 10.762622, "longitude": 106.660172},  # Example coordinates
            "PHYS101": {"latitude": 10.762622, "longitude": 106.660172},
            "CS101": {"latitude": 10.762622, "longitude": 106.660172}
        }
        self.max_distance = 0.1  # Maximum allowed distance in kilometers

    def load_attendance_records(self):
        try:
            with open(self.attendance_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_attendance_records(self, records):
        with open(self.attendance_file, 'w') as f:
            json.dump(records, f, indent=4)

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        """Calculate distance between two points in kilometers"""
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        return geopy.distance.geodesic(coords_1, coords_2).km

    def mark_attendance(self, student_id, class_id, current_lat, current_lon):
        """Mark attendance based on GPS location"""
        # Get class location
        class_location = self.class_locations.get(class_id)
        if not class_location:
            return False, "Invalid class ID"

        # Calculate distance from class location
        distance = self.calculate_distance(
            current_lat, current_lon,
            class_location["latitude"], class_location["longitude"]
        )

        # Determine attendance status
        status = "present" if distance <= self.max_distance else "absent"

        # Create attendance record
        record = AttendanceRecord(
            student_id=student_id,
            class_id=class_id,
            timestamp=datetime.now().isoformat(),
            latitude=current_lat,
            longitude=current_lon,
            status=status
        )

        # Save record
        records = self.load_attendance_records()
        records.append(record.to_dict())
        self.save_attendance_records(records)

        return True, {
            "status": status,
            "distance": distance,
            "max_distance": self.max_distance
        }

    def get_student_attendance(self, student_id, class_id=None):
        """Get attendance records for a student"""
        records = self.load_attendance_records()
        if class_id:
            return [r for r in records if r["student_id"] == student_id and r["class_id"] == class_id]
        return [r for r in records if r["student_id"] == student_id]

    def get_class_attendance(self, class_id):
        """Get attendance records for a class"""
        records = self.load_attendance_records()
        return [r for r in records if r["class_id"] == class_id]

# Example usage
if __name__ == "__main__":
    attendance_manager = AttendanceManager()
    
    # Example: Mark attendance
    success, result = attendance_manager.mark_attendance(
        student_id="ST001",
        class_id="MATH101",
        current_lat=10.762622,
        current_lon=106.660172
    )
    print(f"Attendance marked: {success}")
    print(f"Result: {result}") 

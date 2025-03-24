from flask import Flask, request, jsonify
from attendance_data import AttendanceManager
import Student_account_data
import Manager_account_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
attendance_manager = AttendanceManager()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Read manager data
    mana_data = Manager_account_data.read_data()
    
    # Check if it's a manager login
    if email == mana_data[3] and password == mana_data[1]:
        return jsonify({
            "success": True,
            "role": "manager",
            "id": mana_data[2]
        })
    
    # Check if it's a student login
    student_data = Student_account_data.read_data()
    for student in student_data:
        # student is already a list from read_data()
        if len(student) >= 2 and student[1] == email:  # Check if email matches
            return jsonify({
                "success": True,
                "role": "student",
                "id": student[2] if len(student) > 2 else student[1],  # Use student ID if available, otherwise use email
                "name": student[0]
            })
    
    return jsonify({
        "success": False,
        "message": "Invalid credentials"
    }), 401

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not all([name, email, password]):
        return jsonify({
            "success": False,
            "message": "Missing required fields"
        }), 400
    
    # Check if email already exists
    student_data = Student_account_data.read_data()
    for student in student_data:
        if len(student) >= 2 and student[1] == email:  # Email exists
            return jsonify({
                "success": False,
                "message": "Email already registered"
            }), 400
    
    # Create new student record
    try:
        # Generate a simple student ID (you might want to implement a better ID generation system)
        student_id = f"ST{len(student_data) + 1:03d}"
        
        # Create student record as a list
        student_record = [name, email, student_id]
        
        # Save to file
        Student_account_data.write_data(" ".join(student_record))
        
        return jsonify({
            "success": True,
            "message": "Account created successfully",
            "student_id": student_id
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error creating account: {str(e)}"
        }), 500

@app.route('/api/attendance/mark', methods=['POST'])
def mark_attendance():
    data = request.json
    student_id = data.get('student_id')
    class_id = data.get('class_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    if not all([student_id, class_id, latitude, longitude]):
        return jsonify({
            "success": False,
            "message": "Missing required fields"
        }), 400
    
    success, result = attendance_manager.mark_attendance(
        student_id=student_id,
        class_id=class_id,
        current_lat=latitude,
        current_lon=longitude
    )
    
    return jsonify({
        "success": success,
        "result": result
    })

@app.route('/api/attendance/student/<student_id>', methods=['GET'])
def get_student_attendance(student_id):
    class_id = request.args.get('class_id')
    records = attendance_manager.get_student_attendance(student_id, class_id)
    return jsonify({
        "success": True,
        "records": records
    })

@app.route('/api/attendance/class/<class_id>', methods=['GET'])
def get_class_attendance(class_id):
    records = attendance_manager.get_class_attendance(class_id)
    return jsonify({
        "success": True,
        "records": records
    })

if __name__ == '__main__':
    app.run(debug=True) 

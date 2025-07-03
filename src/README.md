# Mergington High School Activities

A comprehensive web-based activity management system that enables teachers to manage student participation in extracurricular activities at Mergington High School.

## Features

- **View All Activities**: Browse 13+ extracurricular activities with detailed information including schedules, descriptions, and participant counts
- **Advanced Filtering**: Filter activities by category (Sports, Arts, Academic, Community, Technology), day of the week, and time period (Before School, After School, Weekend)
- **Search Functionality**: Search across activity names, descriptions, and schedules
- **Teacher Authentication**: Secure login system for teachers to manage student registrations
- **Student Registration Management**: Teachers can register and unregister students for activities
- **Real-time Capacity Tracking**: View current enrollment and available spots for each activity
- **Weekend & Evening Activities**: Support for activities scheduled on weekends and evening hours
- **Responsive Design**: Modern web interface that works across devices

## For Teachers

Teachers have full control over student activity management through our secure authentication system. Once logged in, teachers can:

- **Register Students**: Add students to any activity with available capacity
- **Manage Enrollments**: View current participant lists and remove students if needed
- **Track Capacity**: Monitor enrollment numbers and available spots across all activities
- **Access All Activities**: View and manage students across all activity categories and time periods

### Request System Changes

Teachers can also request changes to the activities system using our structured issue templates. No technical knowledge required!

📋 **[Create a New Request](https://github.com/ktanino10/skills-expand-your-team-with-copilot/issues/new/choose)**

Available request types:
- 🎯 Add new activities/clubs
- ✏️ Modify existing activities
- ❌ Remove/cancel activities  
- 🐛 Report bugs and issues
- ✨ Request new features
- 👥 Bulk student management
- 💬 General questions

📖 **[Teacher's Guide](../docs/teacher-guide.md)** - Complete guide to using the issue templates

## Technology Stack

- **Backend**: FastAPI (Python) with MongoDB database
- **Frontend**: Modern JavaScript with responsive CSS
- **Authentication**: Teacher login system with session management
- **Database**: MongoDB for activity and user data storage
- **API**: RESTful endpoints for all functionality

## Development Guide

For detailed setup and development instructions, please refer to our [Development Guide](../docs/how-to-develop.md).

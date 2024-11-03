# Med-Bot

Med-Bot is an interactive medical assistance web application that provides three main features:

1. Medical Advice Chat
2. Wound Detection & First Aid
3. Custom Health Recommendations

## Features

### 1. Medical Advice Chat
- Real-time chat interface for medical queries
- Powered by GPT-3.5 for accurate medical information
- Natural conversation flow with typing animations

### 2. Wound Detection
- Upload images of wounds for automatic classification
- Supports multiple wound types:
  - Abrasions
  - Bruises
  - Burns
  - Cuts
  - Ingrown nails
  - Lacerations
  - Stab wounds
- Provides specific first-aid steps for detected wounds
- Uses TensorFlow-based deep learning model for classification

### 3. Custom Health Feature
- Personalized health recommendations including:
  - Medication suggestions
  - Precautionary measures
  - Workout recommendations
  - Dietary advice

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- AI/ML: 
  - OpenAI GPT-3.5
  - TensorFlow for wound detection
- UI Framework: Bootstrap Icons

## Setup

1. Install required Python packages
2. Set up OpenAI API key
3. Run Flask application:
```python
python app.py
```

## Project Structure

- `/templates` - HTML templates
- `/static/assets` - CSS, JavaScript, and other static files
- `/uploaded_images` - Temporary storage for uploaded wound images
- `app.py` - Main Flask application
- `gpt.py` - GPT integration for medical advice
- `main.py` - Wound detection model implementation

## Note

This is a prototype medical assistance tool. Always consult healthcare professionals for serious medical concerns.
```
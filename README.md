# Financial Expert Finder

A modern platform to connect businesses with accounts receivable (AR) specialists, built for JustPaid.ai's hackathon.

## Features
- **User Profiles**: Detailed profiles for businesses and AR experts.
- **Advanced Search**: Filter experts by location, expertise, and ratings.
- **Quote Requests**: Businesses can request services from experts.
- **Reviews & Ratings**: Build trust with user feedback.
- **AI Chatbot**: Assists users with navigation and FAQs.
- **NLP Matching**: Matches businesses with experts using AI embeddings.

## Tech Stack
- **Frontend**: Next.js, TypeScript, Tailwind CSS, Radix UI
- **Backend**: Django, Python, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Auth0
- **AI**: OpenAI API, Sentence Transformers

## Setup Instructions

### Prerequisites
- Node.js, npm
- Python, pip
- PostgreSQL
- Auth0 account
- OpenAI API key

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
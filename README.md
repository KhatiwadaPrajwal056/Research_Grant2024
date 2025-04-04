# Skin Cancer Detection App

A Streamlit-based web application for skin cancer detection using AI.

## Features

- Upload skin images for analysis
- AI-powered skin lesion detection and classification
- Detailed results with confidence scores
- Educational information about skin cancer types

## Setup Instructions

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/skin-cancer-detection.git
   cd skin-cancer-detection
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your API credentials:
   ```
   API_URL=your_api_url_here
   HF_API_TOKEN=your_huggingface_token_here
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

### Deploying to Vercel

1. Push your code to GitHub

2. Connect your GitHub repository to Vercel

3. Configure the environment variables in the Vercel dashboard:
   - `API_URL`
   - `HF_API_TOKEN`

4. Deploy using the Vercel Python framework

## Project Structure

```
skin-cancer-detection/
├── .env                    # Environment variables (not in git)
├── .gitignore              # Git ignore file
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── vercel.json             # Vercel configuration
├── app.py                  # Main entry point
├── utils/
│   ├── __init__.py
│   └── api.py              # API handling functions
├── components/
│   ├── __init__.py
│   ├── header.py           # Header component
│   ├── image_upload.py     # Image upload component
│   ├── results.py          # Results display component
│   └── about.py            # About section component
├── static/
│   ├── css/
│   │   └── style.css       # CSS styles
│   └── images/
│       └── placeholder.png # Placeholder images
```

## Authors

- Iza KC
- Prajwal Khatiwada
- Samrat Adhikari
- Er. Pralhad Chapagain

## Disclaimer

This tool is for educational purposes only and should not be considered medical advice. Always consult with a qualified healthcare provider.

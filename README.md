# Speech-To-Text CLI Tool

A simple command-line tool to transcribe audio files using [AssemblyAI](https://www.assemblyai.com/) and automatically uploads the transcript to Google Docs. Supports advanced features like speaker diarization and key terms prompting (with the slam-1 model).

## Features
- Transcribe audio files with [AssemblyAI](https://www.assemblyai.com/dashboard/signup)
- Automatic upload the transcript to Google Docs and get a shareable link
- Supports speaker diarization (who said what)
- Supports key terms prompting with the slam-1 model


## Quickstart: Setup Steps

1. **Google Cloud Setup**
   - Create a project, enable Google Docs API, configure OAuth consent screen, create OAuth credentials, download and rename `credentials.json`, add yourself as a test user.
2. **AssemblyAI Setup**
   - Sign up and get your API key.
3. **Create and fill out your `.env` file**
   - Add your AssemblyAI and Google credentials.
4. **Install Python dependencies**
   - Use a virtual environment and `pip install -r requirements.txt`.
5. **(Optional but recommended) Set up the CLI command**
   - Add your project directory to your `PATH` or create a symlink for global access.
6. **Run the tool!**
   - Use `transcribe /path/to/audiofile.mp3` from anywhere.

## Setup Instructions

### 1. Clone the Repository & Install Dependencies
```sh
cd /path/to/your/project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. AssemblyAI API Key
- Go to the [AssemblyAI Dashboard](https://www.assemblyai.com/app/dashboard)
- Copy your API key
- Create a `.env` file in your project directory:
  ```env
  ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here
  GOOGLE_CLIENT_ID=your_client_id_here
  GOOGLE_CLIENT_SECRET=your_client_secret_here
  ```

### 3. Google Cloud Setup
#### a. Create a Google Cloud Project
- Go to the [Google Cloud Console](https://console.cloud.google.com/)
- [Create a new project](https://console.cloud.google.com/projectcreate) (or use an existing one)

#### b. Enable Google Docs API
- Go to [APIs & Services > Library](https://console.cloud.google.com/apis/library)
- [Search for Google Docs API](https://console.cloud.google.com/apis/library/docs.googleapis.com)
- Click **Enable**

#### c. Configure OAuth Consent Screen
- Go to APIs & Services > OAuth consent screen > Branding and fill out the *App Name*, *User Support Email*, *Developer contact information*
- Save and continue

#### d. Create OAuth 2.0 Credentials and Download credentials.json
- Go to [APIs & Services > Credentials](https://console.cloud.google.com/apis/credentials)
- Click **+ Create Credentials > OAuth client ID**
- Choose **Desktop app**
- Name it and click **Create**
- **Download the `client_secret_...json` file** (this is your OAuth client secret)
- **Rename the file to `credentials.json`**
- **Move `credentials.json` into your project directory** (the same folder as your code)

> **Important:** The `credentials.json` file is required for Google Docs integration. If it is missing or not in the project directory, Google Docs upload will fail.

#### e. Add Yourself as a Test User
- Go to APIs & Services > OAuth consent screen > Audience 
- Scroll to **Test users**
- Click **+ Add users** and enter your Google account email
- Save

### 4. (Optional but Recommended) Set Up the CLI Command

**To run `transcribe` from anywhere:**

- **Make the script executable:**
  ```sh
  chmod +x /path/to/your/project/transcribe
  ```
- **Option 1: Add your project directory to your PATH**
  - Add this line to your `~/.zshrc` or `~/.bashrc`:
    ```sh
    export PATH="$PATH:/path/to/your/project"
    ```
  - Then restart your terminal or run `source ~/.zshrc`.
- **Option 2: Create a symlink in `/usr/local/bin`:**
  ```sh
  sudo ln -s /path/to/your/project/transcribe /usr/local/bin/transcribe
  ```
  Now you can run `transcribe ...` from anywhere.

### 5. First Run: Authorize Google Docs
- Run the tool for the first time. A browser window will open for you to log in and authorize access to your Google account.
- Approve the requested permissions.

## Usage

### Basic Transcription (with diarization):
```sh
transcribe /path/to/audiofile.mp3
```

### Slam-1 Model with Key Terms Prompting:
```sh
transcribe /path/to/audiofile.mp3 --slam --keyterms "term1" "term2" ...
```

- The tool will print the transcript and a link to the Google Doc.

## Notes
- Your `.env` file is for the AssemblyAI API key. Google Docs API **requires** the `credentials.json` file for OAuth. This file must be in your project directory.
- You only need to add yourself as a test user once per project.
- If you want to use another Google account, add it as a test user (you get up to 100 test users).
- [AssemblyAI Docs](https://www.assemblyai.com/docs/)
- [Google Docs API Docs](https://developers.google.com/docs/api/quickstart/python)

## License
MIT 
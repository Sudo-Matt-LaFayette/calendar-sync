# calendar-sync
Sure, here's a detailed explanation of the "calendar-sync" repository:

### 📂 Files and Structure:
- **`calendar-sync.py`**: The main script responsible for the synchronization process.
- **`requirements.txt`**: Lists the dependencies required for the script to run.
- **`README.md`**: Provides an overview, setup instructions, and usage guidelines.

### ⚙️ Functionality:
- **Google Calendar Integration**: Uses Google Calendar API to fetch and update calendar events.
- **ToDoist Integration**: Uses ToDoist API to fetch and update tasks.
- **Synchronization Logic**: Ensures that events in Google Calendar and tasks in ToDoist are kept in sync, creating, updating, or deleting items as necessary.

### 🛠️ Setup and Usage:
1. **Installation**:
   - Clone the repository.
   - Install dependencies using `pip install -r requirements.txt`.
2. **Configuration**:
   - Set up API credentials for Google Calendar and ToDoist.
   - Configure the script with these credentials.
3. **Running the Script**:
   - Execute `calendar-sync.py` to start the synchronization process.

### 🔍 Additional Details:
- **Authentication**: OAuth2 is used for authenticating with Google Calendar and ToDoist APIs.
- **Error Handling**: Includes basic error handling to manage API rate limits and connectivity issues.

For more details and to access the code, visit the [repository](https://github.com/Sudo-Matt-LaFayette/calendar-sync).

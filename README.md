# Smart AI Crop Recommendation System

## Database configuration

The application connects to a local MySQL database named `smart_crop_db` as
`root`. Create the database and the tables used by `database/save_records.py`,
then set the database password in your environment before starting the application.
The password is read from `MYSQL_PASSWORD` and is not stored in this repository.

In PowerShell, set it for the current terminal session with:

```powershell
$env:MYSQL_PASSWORD = "your-local-mysql-password"
```
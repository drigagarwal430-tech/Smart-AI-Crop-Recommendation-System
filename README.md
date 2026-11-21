# Smart AI Crop Recommendation System

## Run on Windows

From the project directory, apply the schema in MySQL Workbench by opening and
executing `database/schema.sql` as the local `root` user. It creates the database
and tables if they do not exist; it does not drop existing tables or records.

In PowerShell, set the MySQL password for this run and launch Streamlit from the
project virtual environment. The password is not saved in the repository:

```powershell
$securePassword = Read-Host "MySQL root password" -AsSecureString
$passwordPointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($securePassword)
try {
    $env:MYSQL_PASSWORD = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($passwordPointer)
}
finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($passwordPointer)
}

.\venv\Scripts\python.exe -m streamlit run app.py
```

If Streamlit is already running, stop it with `Ctrl+C` and restart it from the
PowerShell session where `MYSQL_PASSWORD` is set. After stopping the app, clear
the variable with `$env:MYSQL_PASSWORD = $null`.
#define SourcePath "dist/pdf-encryptor"
#define MyAppName "PDF Encryptor"
#define MyAppExeName "pdf-encryptor.exe"

[Setup]
AppName={#MyAppName}
AppVersion=1.5
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}

[Files]
Source: "{#SourcePath}/*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}";

[Icons]
Name: "{userdesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

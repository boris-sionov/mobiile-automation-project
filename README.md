# mobiile-automation-project


## 🚀 Getting Started

In order to start the automation process,  
clone the code using the command below:
## 🚀 Getting Started

In order to start the automation process,  
clone the code using the command below:

```bash
git clone https://github.com/boris-sionov/mobiile-automation-project
```


## 📦 Install Dependencies

After cloning the project, install the required packages using:
```bash
cd configuration
pip install -r requirements.txt
```

## ⚙️ Configure Settings

After installing dependencies, make sure to update the `config.ini` file with the correct values:

```ini
[capabilities]
platform_name = 
platform_version = 
automation_name = 
device_name = 
app_path = utilities/Android_Demo_App.apk
app_package = com.code2lead.kwad
app_activity = com.code2lead.kwad.MainActivity
appium_server = http://127.0.0.1:4723


[date]
logs_time_format = %%d/%%b/%%Y %%H:%%M:%%S %%A
files_time_format = %%d-%%b-%%Y %%H:%%M:%%S


[web]
url = none
browser = none

[general]
timeout = 5
; Choose web for browsers. iOS for iPhone/iPad. Android for Android phone/tablet
platform = Android

```

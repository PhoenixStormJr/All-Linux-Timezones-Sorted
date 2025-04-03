import subprocess
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def GetOutputOfCommand(command):
    result = subprocess.check_output(command.split(' '))
    result = result.decode('utf-8')
    return result

def RunCommand(command):
    subprocess.run(command.split(" ")) 


timezones = open("timezones.txt","r",encoding='utf-8').read().strip().split('\n')
TimeZoneDataFile = open("TimeZoneData.txt","w",encoding='utf-8')

for timezone in timezones:
    try: result = GetOutputOfCommand(f'sudo timedatectl set-timezone {timezone}')
    except:
        try: result = GetOutputOfCommand(f'sudo timedatectl set-timezone {timezone}')
        except:
            try: result = GetOutputOfCommand(f'sudo timedatectl set-timezone {timezone}')
            except:
                result = f"Failed to set time zone: Invalid or not installed time zone '{timezone}'"
    time1 = GetOutputOfCommand("date")    
    print(f"\"{result}\"")
    if(result == ""):
        TimeZoneDataFile.write(timezone+"\n")
        TimeZoneDataFile.write(time1+"\n\n")

TimeZoneDataFile.close()
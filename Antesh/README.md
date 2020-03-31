# Antesh
Helper class to Activate a specific Anaconda environment &amp; Run python script from PHP file.

# How to use
- To Activate a specific Anaconda environment [UPDATE Config Section]
```
$_cmd_src = 'c:\WINDOWS\system32\cmd.exe'

//Path to Anaconda activate.bat file
$_conda_act = 'C:\Users\PCNAME\Anaconda3\Scripts\activate.bat'

//environment name
$_env_name = 'env_name'

//Python version (of the desired env)
$_python = 'C:\Users\PCNAME\Anaconda3\envs\env_name\python.exe'
```
- Activate Anaconda environment & Run Python script
```
$antesh_obj = new Antesh('C:\Users\PCNAME\Desktop\test.py');
```
- Pass ARGS as an array
```
$antesh_obj = new Antesh('C:\Users\PCNAME\Desktop\test.py', array('arg1', 'arg2', '..'));
```

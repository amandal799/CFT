## **CFT**

> A terminal based application for extracting information from codeforces related to problems , contests , users, etc.

## Getting  Started
> clone or download it and then from terminal run **_codeforces.py_** file.  
Make sure you run it with python3 and you have all the necessary packages installed .

### **Prerequisites**
>   Python3.x

### Python Libraries to be installed :-
> * **requests** package
> * **bs4** (BeautifulSoup)
> * **termcolor** (Not necessary though unless you want texts to be colored)

## How to use it
> This is for those who have got the application up and running :-
### commands :-
> For problem list  :-
* **plist**  

> it can be followed by any combination of the following commands:-
1. **{-u | -h}** followed by any user's handle
>
2. **{-tags}** followed by tags separated by space
 >
3. **{-type}** followed by type of questions in codeforces like A,B,C,D (case-insensitive)
>
4. **{-pname}** followed by a list problem names
  * if you want all the problems which contain **socks** in it the you just write **plist -pname socks**
  * if vanya , tables should be in the name of the problem then you should write vanya&tables
>  
5. **{-verdict}** followed by ok,wrong,failed,etc for user-specific problems

> For Problem statement :-  
* **pstmt**

>it must be followed by follwing :-
1. **{-pid}** followed by valid problem ids like 917A 1B 456D
>
### Examples :-
>
1. To get all the problems with tag dp and dfs and of type D and E solved by tourist  
  #### **command**  
  **_plist -u tourist -tags dp dfs -type D E_**
>
2. To get all the problems which contain pokemon in it  
#### **command**  
**_plist -pname pokemon_**
>
3. To get the statement of problem 917D
#### **command**
**_pstmt -pid 917D_**

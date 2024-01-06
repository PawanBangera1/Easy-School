import mysql.connector
import streamlit as st

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pawan1"
)
mycursor = mydb.cursor()
print("Connection Established")

# Create Streamlit App

def main():
    st.title("Student Data");

    # Display Options for CRUD Operations
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))
    # Perform Selected CRUD Operations
    if option == "Create":
        st.subheader("Create a Record")
        name = st.text_input("Enter Name")
        USN = st.text_input("Enter USN")
        email = st.text_input("Enter Email")
        Phone_Number = st.text_input("Enter Phone Number")
        age = st.text_input("Enter age")

        #gender = st.text_input("Enter gender [Male | Female | Others]")
        gender = ("male", "female", "Others")
        op = st.radio("Enter gender [Male | Female | Others]", gender)

        # Perform Selected CRUD Operations
        if op == "male":
            gender = 'male'
        elif op == 'female':
            gender = 'female'
        elif op == 'others':
            gender = 'others'

        if st.button("Create"):
            sql = "insert into users(name,USN,email,Phone_Number,age,gender) values(%s,%s,%s,%s,%s,%s)"
            val = (name, USN, email, Phone_Number, age, gender)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")

    elif option == "Read":
        st.subheader("Read Records")
        mycursor.execute("select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Update":
        st.subheader("Update a Record")
        id = int(st.number_input("Enter ID", min_value=1))
        name = st.text_input("Enter Name")
        USN = st.text_input("Enter USN")
        email = st.text_input("Enter Email")
        Phone_Number = st.text_input("Enter Phone Number")
        age = st.text_input("Enter age")

        #gender = st.text_input("Enter gender [Male | Female | Others]")
        gender = ("male", "female", "Others")
        op = st.radio("Enter gender [Male | Female | Others]", gender)

        # Perform Selected CRUD Operations
        if op == "male":
            gender = 'male'
        elif op == 'female':
            gender = 'female'
        elif op == 'others':
            gender = 'others'

        if st.button("Update"):
            sql = "update users set name=%s, USN=%s,email=%s,Phone_Number=%d,age=%d,gender=%s where id =%s"
            val = (name, USN, email, Phone_Number, age, gender, id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")

    elif option == "Delete":
        st.subheader("Delete a Record")
        id = st.number_input("Enter ID", min_value=1)
        if st.button("Delete"):
            sql = "delete from users where id =%s"
            val = (id,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")

if __name__ == "__main__":
    main()
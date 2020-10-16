# Definig a function swapFile to change data from one file to another 
def swapFile():
    # Creating inputs for the user to write the file name and extension " Example.txt "
    # Getting the file name "A" from the user by input
    fileA = input("Enter the file name from which you want to take data : ")
    # Getting the file name "B" from the user by input
    fileB = input("Enter the file name with which you want to exchange data : ")
    
    # Getting data from file "A"
    dataA = open(fileA, "r")
    # Getting data from file "B"
    dataB = open(fileB, "r")
    
    # Reading and storing the data of file "A"
    data_a = dataA.read()
    # Reading and storing the data of file "B"
    data_b = dataB.read()

    # Creating another variable to access the writing mode for file "A"
    changeDataA = open(fileA, "w")
    # Creating another variable to access the writing mode for file "B"
    changeDataB = open(fileB, "w")

    # The Magic of swapping takes place here 
    # Changing the data from file "B" to file "A"
    changeDataA.write(data_b)
    # Changing the data from file "A" to file "B"
    changeDataB.write(data_a)
    

# Calling the function so that we dont get an empty result
swapFile()


#  !       !     !    !       !  ! ! ! ! !        ! ! ! ! !  !       !  !       !
#  !       !    ! !    !     !   !                !          !       !  ! !     !                           
#  ! ! ! ! !   ! ! !    !   !    ! ! ! ! !        ! ! ! ! !  !       !  !   !   !                            
#  !       !  !     !    ! !     !                !          !       !  !     ! !                     
#  !       ! !       !    !      ! ! ! ! !        !          ! ! ! ! !  !       !                                          
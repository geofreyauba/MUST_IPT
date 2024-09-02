from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    """
    Render the home page.
    """
    return render(request, 'employeeapp/index.html')

def signup(request):
    """
    Handle user signup and automatically log in the user after successful registration.
    """
    if request.method == "POST":
        # Retrieve form data from POST request
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        # Validate that passwords match
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return render(request, 'employeeapp/signup.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'employeeapp/signup.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'employeeapp/signup.html')

        # Create a new user if all validations pass
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Automatically log in the newly registered user
        login(request, user)
        messages.success(request, "You are now registered and logged in.")
        return redirect("home")

    # Render the signup form for GET request
    return render(request, 'employeeapp/signup.html')

def signin(request):
    """
    Handle user sign-in.
    """
    if request.method == "POST":
        # Retrieve form data from POST request
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # Check if authentication is successful
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("home")  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password.")
    
    # Render the signin form for GET request
    return render(request, 'employeeapp/signin.html')

def signout(request):
    """
    Handle user sign-out and redirect to the home page.
    """
    if request.method == "POST":
        # Log out the currently logged-in user
        logout(request)
        # Show a success message indicating that the user has been logged out
        messages.success(request, "You have been logged out.")
        # Redirect to the home page after logging out
        return redirect("home")
    
    # Redirect to home page for GET request
    return redirect("home")

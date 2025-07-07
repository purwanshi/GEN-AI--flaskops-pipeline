import google.generativeai as genai
import subprocess

# Set your Gemini API key
genai.configure(api_key="AIzaSyAsCrjzevYWOnRZMW4hVdERmkpoZ6VckP4")

# Welcome message
print("\n\t🚀 Welcome to Gemini AI Code Generator")
print("---------------------------------------------\n")

# Take prompt from user
user_prompt = input("Describe the code you want me to generate:\n> ")

# Load Gemini model
model = genai.GenerativeModel('gemini-pro')

# Send user prompt to Gemini
response = model.generate_content(user_prompt)

# Extract generated code
generated_code = response.text

# Display generated code
print("\n🔧 Generated Code:\n")
print(generated_code)

# Save generated code to a .py file
with open("generated_app.py", "w") as file:
    file.write(generated_code)

print("\n✅ Code saved to generated_app.py")

# Run the generated code using subprocess
print("\n▶️  Running generated_app.py...\n")

run_status = subprocess.getstatusoutput("python3 gen-ai-ops_app.py")

# Show output or error
if run_status[0] == 0:
    print("🎉 Output:\n", run_status[1])
else:
    print("❌ Error:\n", run_status[1])

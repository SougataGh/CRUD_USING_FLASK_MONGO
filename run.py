from app import create_app

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == "__main__":
    # Run the app on the default host and port (5000)
    app.run(debug=True, host='0.0.0.0', port=5000)

from app import app
import routes_minimal as routes  # Use minimal routes for fast startup

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Helper to reset activities (since in-memory DB is shared)
def reset_activities():
    app.dependency_overrides = {}
    # Optionally, reload the module or reset the dict if needed


def test_get_activities():
    # Arrange
    # (No setup needed for read-only test)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_success():
    # Arrange
    test_email = "testuser1@mergington.edu"
    activity = "Chess Club"
    # Remove if already present (directly manipulate in-memory DB for test isolation)
    from src.app import activities
    if test_email in activities[activity]["participants"]:
        activities[activity]["participants"].remove(test_email)

    # Act
    response = client.post(f"/activities/{activity}/signup?email={test_email}")

    # Assert
    assert response.status_code == 200
    assert f"Signed up {test_email}" in response.json()["message"]


def test_signup_duplicate():
    # Arrange
    test_email = "testuser2@mergington.edu"
    activity = "Programming Class"
    client.post(f"/activities/{activity}/signup?email={test_email}")

    # Act
    response = client.post(f"/activities/{activity}/signup?email={test_email}")

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_signup_nonexistent_activity():
    # Arrange
    test_email = "ghost@mergington.edu"
    activity = "Nonexistent Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={test_email}")

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

# Add more tests as endpoints are added (e.g., DELETE for unregister)

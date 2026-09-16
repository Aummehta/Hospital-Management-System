import pytest
from fastapi.testclient import TestClient
from main import app

def test_get_all_patients():
    with TestClient(app) as client:
        response = client.get("/AllPatient")
        assert response.status_code == 200
        json_resp = response.json()
        assert json_resp["status"] == "ok"
        assert "data" in json_resp
        assert "AllPatientData" in json_resp["data"]
        assert isinstance(json_resp["data"]["AllPatientData"], list)

def test_all_patient_name_email():
    with TestClient(app) as client:
        response = client.get("/AllPatientNameEmail")
        assert response.status_code == 200
        json_resp = response.json()
        assert json_resp["status"] == "ok"
        assert "data" in json_resp
        assert "AllPatientNameEmail" in json_resp["data"]
        assert isinstance(json_resp["data"]["AllPatientNameEmail"], list)

def test_get_all_medicine():
    with TestClient(app) as client:
        response = client.get("/AllMedicine")
        assert response.status_code == 200
        json_resp = response.json()
        assert json_resp["status"] == "ok"
        assert "data" in json_resp
        assert "AllMedicine" in json_resp["data"]
        assert isinstance(json_resp["data"]["AllMedicine"], list)



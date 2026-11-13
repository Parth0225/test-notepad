def test_create_list_get_update_delete(client):
    r = client.post("/notes/", json={"title": "First"})
    assert r.status_code == 201
    note_id = r.json()["id"]
    assert client.get("/notes/").json()[0]["title"] == "First"
    assert client.get(f"/notes/{note_id}").json()["title"] == "First"
    assert client.put(f"/notes/{note_id}", json={"title": "Renamed"}).json()["title"] == "Renamed"
    assert client.delete(f"/notes/{note_id}").status_code == 204
    assert client.get(f"/notes/{note_id}").status_code == 404


def test_validation(client):
    assert client.post("/notes/", json={}).status_code == 422

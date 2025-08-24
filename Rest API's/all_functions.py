import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# 1️⃣ GET — Fetch a list of posts
print("---- GET ----")
res = requests.get(BASE_URL)
print("Status:", res.status_code)
print("First Post:", res.json()[0])  # Print only first post for readability


# 2️⃣ POST — Create a new post
print("\n---- POST ----")
new_post = {"title": "My New Post", "body": "This is the content", "userId": 1}
res = requests.post(BASE_URL, json=new_post)
print("Status:", res.status_code)
print("Created Post:", res.json())
post_id = res.json()["id"]  # Save created post ID


# 3️⃣ PUT — Replace the post (update all fields)
print("\n---- PUT ----")
updated_post = {
    "id": post_id,
    "title": "Updated Post",
    "body": "This post has been fully replaced",
    "userId": 1
}
res = requests.put(f"{BASE_URL}/{post_id}", json=updated_post)
print("Status:", res.status_code)

try:
    print("Replaced Post:", res.json())
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON. Raw response:")
    print(res.text)

# 4️⃣ PATCH — Update only some fields
print("\n---- PATCH ----")
patch_data = {"title": "Patched Title Only"}
res = requests.patch(f"{BASE_URL}/{post_id}", json=patch_data)
print("Status:", res.status_code)
print("Patched Post:", res.json())


# 5️⃣ DELETE — Remove the post
print("\n---- DELETE ----")
res = requests.delete(f"{BASE_URL}/{post_id}")
print("Status:", res.status_code)  # Usually 200 or 204
print("Deleted (empty response expected):", res.text)

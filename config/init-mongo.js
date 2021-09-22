db.createUser(
    {
        user: "citadel",
        pwd: "citadel",
        roles: [
            {
                role: "readWrite",
                db: "citadel"
            }
        ]
    }
)

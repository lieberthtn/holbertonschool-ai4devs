function findUserById(users, id) {
    let foundUser = null;
    for (let i = 0; i < users.length; i++) {
        if (users[i].id === id) {
            foundUser = users[i];
            break;
        }
    }
    if (foundUser) {
        console.log("Found user: " + foundUser.name);
    } else {
        console.log("User not found.");
    }
    return foundUser;
}

const userList = [{id: 1, name: "Ali"}, {id: 2, name: "Veli"}];
findUserById(userList, 3);

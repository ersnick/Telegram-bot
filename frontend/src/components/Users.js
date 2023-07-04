import React from "react"
import User from "./User.js"

function Users({users, handleEdit}) {
    if (users.length > 0)
        return (
            <div>
                {users.map((user) => (
                    <User key={user.id} user={user} handleEdit={handleEdit}/>
                ))}
            </div>
        )
    else
        return (
            <div className="user">
                <h3>Пользователей нет</h3>
            </div>
        )
}

export default Users
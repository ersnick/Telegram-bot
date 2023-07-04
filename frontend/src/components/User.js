import React, {useState} from "react"
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faPenToSquare} from '@fortawesome/free-solid-svg-icons'
import EditForm from "./EditForm.js"

function User({user, handleEdit}) {
    const [edit, setEdit] = useState(false);
    const [surname, setSurname] = useState(user.surname);
    const [name, setName] = useState(user.name);
    const [group, setGroup] = useState(user.group);
    const [patronymic, setPatronymic] = useState(user.patronymic);
    const [renderUser, updateUser] = useState(user)


    const [unchecked, setCheck] = useState(false)
    const checkHandleClick = () => {
        setCheck(!unchecked);
    };

    const [notReject, setReject] = useState(false)
    const rejectHandleClick = () => {
        setReject(!notReject)
    };
    return (
        <div className="user">
            <button className="rejectBtn" onClick={rejectHandleClick}>{notReject ? "Отклонено" : "Отклонить"}</button>
            <button className="checkBtn" onClick={checkHandleClick}>{unchecked ? "Принято" : "Принять"}</button>
            <FontAwesomeIcon icon={faPenToSquare} onClick={() => {
                setEdit(!edit);
            }} className="editBtn"
                title="Редактировать"/>
            <h3>{surname} {name} {patronymic} {group}</h3>

            {edit && <EditForm handleEdit={handleEdit} user={renderUser} updateUser={updateUser}
                setUserName={setName} setUserSurname={setSurname} setUserPatronymic={setPatronymic} setUserGroup={setGroup}/>}

        </div>
    )
}

export default User
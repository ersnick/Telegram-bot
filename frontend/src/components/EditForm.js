import React, { useState } from "react";

function EditForm({user, updateUser, setUserName, setUserGroup, setUserPatronymic, setUserSurname}) {

  const [isOpen, setIsOpen] = useState(true);
  const [surname, setSurname] = useState(user.surname);
  const [name, setName] = useState(user.name);
  const [group, setGroup] = useState(user.group);
  const [patronymic, setPatronymic] = useState(user.patronymic);

  const handleSurname = function (e) {
    setSurname(e.target.value);
  };

  const handleName = function (e) {
    setName(e.target.value);
  };

  const handlePatronymic = function (e) {
    setPatronymic(e.target.value);
  };

  const handleGroup = function (e) {
    setGroup(e.target.value);
  };

  const handleSave = function () {
    setUserSurname(surname)
    setUserName(name)
    setUserPatronymic(patronymic)
    setUserGroup(group)

    updateUser(user)

    setIsOpen(false); 
  };

  const handleCancel = function () {
//    setSurname(tempSurname);
//    setName(tempName);
//    setPatronymic(tempPatronymic);
//    setGroup(tempGroup);

    setIsOpen(false); 
  };

  if (!isOpen) {
    return null; 
  }

  return (
    <form id="editForm" className={"form-edit-statement"}>
      <input
        type="text"
        placeholder="Фамилия"
        value={surname}
        onChange={handleSurname}
      />
      <input
        type="text"
        placeholder="Имя"
        value={name}
        onChange={handleName}
      />
      <input
        type="text"
        placeholder="Отчество"
        value={patronymic}
        onChange={handlePatronymic}
      />
      <input
        type="text"
        placeholder="Группа"
        value={group}
        onChange={handleGroup}
      />
      <button type="button" className="Edit" onClick={handleSave}>
        Сохранить
      </button>
      <button type="button" className="Edit" onClick={handleCancel}>
        Отменить
      </button>
    </form>
  );
}

export default EditForm;

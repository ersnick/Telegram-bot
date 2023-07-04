import React from "react";
import { useState } from "react";

function SendForm(){

  const [showList, setShowList] = useState(false);
  const [showStudentList, setShowStudentList] = useState(false);
  const [textInput, setTextInput] = useState("");
  const [selectedImage, setSelectedImage] = useState(null);

  const handleCheckboxChange = () => {
    setShowList(!showList);
  };

  const handleStudentCheckboxChange = () => {
    setShowStudentList(!showStudentList);
  };

  const handleTextChange = (event) => {
    setTextInput(event.target.value);
  };

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleImageRemove = () => {
    setSelectedImage(null);
  };

  const handleSubmit = () => {
    console.log("Отправлено!");
    console.log("Текст:", textInput);
    console.log("Изображение:", selectedImage);
  };

  return (
    <div>
      <input
        id="upload-btn"
        type="file"
        name="myImage"
        onChange={handleImageChange}
      />
      {selectedImage && (
        <div>
          <button id="deleteButton" onClick={handleImageRemove}>
            Удалить
          </button>
        </div>
      )}
      <textarea
        placeholder="Enter text..."
        type="text"
        className="inputText"
        value={textInput}
        onChange={handleTextChange}
      ></textarea>
      <h3 className="recipient">Выбрать получателя:</h3>

      <label>
        <input
          type="checkbox"
          className="chooseRecipient"
          onChange={handleCheckboxChange}
        />
        Группа
      </label>

      {showList && (
        <div id="checkbox-list">
          <label>
            <input type="checkbox" />
            ПрИ-101
          </label>
          <label>
            <input type="checkbox" />
            ПрИ-102
          </label>
        </div>
      )}

      <label>
        <input
          type="checkbox"
          className="chooseRecipient"
          onChange={handleStudentCheckboxChange}
        />
        Студент
      </label>

      {showStudentList && (
        <div id="checkbox-list-two">
          <label>
            <input type="checkbox" />
            ПрИ-101
          </label>
          <label>
            <input type="checkbox" />
            ПрИ-102
          </label>
        </div>
      )}

      <button onClick={handleSubmit}>Отправить</button>
    </div>
  )

}

export default SendForm
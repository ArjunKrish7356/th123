import React, { useState } from 'react';
import axios from 'axios';
import { ReactMic } from 'react-mic';

function App() {
  const [record, setRecord] = useState(false);
  const [file, setFile] = useState(null);

  const startRecording = () => {
    setRecord(true);
  }

  const stopRecording = () => {
    setRecord(false);
  }

  const onData = (recordedBlob) => {
    console.log('chunk of real-time data is: ', recordedBlob);
  }

  const onStop = (recordedBlob) => {
    console.log('recordedBlob is: ', recordedBlob);
    setFile(new File([recordedBlob.blob], 'recordedAudio.webm'));
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();

    // Append the file to the form data
    formData.append('file', file);

    // Use axios to post a value to the backend
    axios.post('http://127.0.0.1:8000/translate', formData)
      .then(response => {
        console.log('Response:', response.data); // Handle the successful response here
      })
      .catch(error => {
        console.error('Error:', error); // Handle any errors that occurred during the request
      });
  }

  return (
    <div>
      <ReactMic
        record={record}
        className="sound-wave"
        onStop={onStop}
        onData={onData}
        strokeColor="#000000"
        backgroundColor="#FF4081" />
      <button onClick={startRecording} type="button">Start</button>
      <button onClick={stopRecording} type="button">Stop</button>
      <form onSubmit={handleSubmit}>
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default App;
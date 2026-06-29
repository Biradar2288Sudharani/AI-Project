import { useState } from "react";

function App() {

  const [summary, setSummary] = useState("");
  const [filePath, setFilePath] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);

  // Upload PDF
  const uploadPDF = async () => {

    try {

      if (!selectedFile) {
        alert("Please select a PDF first");
        return;
      }

      const formData = new FormData();

      formData.append(
        "file",
        selectedFile
      );

      const response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      console.log(data);

      setFilePath(
        data.file_path
      );

      alert(
        "PDF Uploaded Successfully"
      );

    } catch (error) {

      console.error(error);

      alert(
        "Upload Failed"
      );
    }
  };

  // Generate Summary
  const generateSummary = async () => {

    try {

      if (!filePath) {

        alert(
          "Please upload PDF first"
        );

        return;
      }

      const response = await fetch(
        "http://127.0.0.1:8000/generate-summary",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify({
            file_path: filePath,
          }),
        }
      );

      const data =
        await response.json();

      console.log(data);

      setSummary(
        data.summary
      );

    } catch (error) {

      console.error(error);

      alert(
        "Failed to generate summary"
      );
    }
  };

  return (
    <div className="min-h-screen bg-slate-100">

      {/* Header */}
      <div className="bg-blue-700 text-white p-6 shadow-lg">

        <h1 className="text-3xl font-bold">
          DScribe AI Discharge Summary Agent
        </h1>

        <p className="text-sm mt-2">
          AI Powered Clinical Discharge Summary Generator
        </p>

      </div>

      {/* Main Container */}
      <div className="max-w-6xl mx-auto p-6">

        {/* Upload Section */}
        <div className="bg-white rounded-xl shadow-md p-6 mb-6">

          <h2 className="text-xl font-semibold mb-4">
            Upload Clinical Document
          </h2>

          <input
            type="file"
            className="border p-2 rounded w-full"
            onChange={(e) => {
              setSelectedFile(
                e.target.files[0]
              );
            }}
          />

          <button
            onClick={uploadPDF}
            className="mt-4 bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
          >
            Upload PDF
          </button>

        </div>

        {/* Generate Summary */}
        <div className="bg-white rounded-xl shadow-md p-6 mb-6">

          <h2 className="text-xl font-semibold mb-4">
            Generate Summary
          </h2>

          <button
            onClick={generateSummary}
            className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700"
          >
            Generate Summary
          </button>

        </div>

        {/* Summary Output */}
        <div className="bg-white rounded-xl shadow-md p-6">

          <h2 className="text-xl font-semibold mb-4">
            Discharge Summary Output
          </h2>

          <textarea
            value={summary}
            onChange={(e) =>
              setSummary(
                e.target.value
              )
            }
            rows="20"
            className="w-full border rounded p-4"
            placeholder="Generated summary will appear here..."
          />

        </div>

      </div>

    </div>
  );
}

export default App;
document.getElementById("fileForm").addEventListener("submit", async function (e) {
    e.preventDefault(); // Evita o reload da página

    const formData = new FormData();
    const file = document.getElementById("file").files[0];
    const fileFormat = document.getElementById("file_format").value;

    if (!file) {
        alert("Por favor, selecione um arquivo!");
        return;
    }

    formData.append("file", file);
    formData.append("file_format", fileFormat);

    try {
        const response = await fetch("http://localhost:5000/convert", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            throw new Error("Erro ao converter o arquivo. Tente novamente.");
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);

        // Exibir o link para download
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `
        <p>Arquivo convertido com sucesso! <a href="${url}" download="converted_file">Baixar Arquivo</a></p>
      `;
    } catch (error) {
        alert(error.message);
    }
});

/*Function that Builds the Table from JSON array*/
function buildTable(output) {
    var table = document.getElementById('myTable');
    table.innerHTML = '';
    for (var i = 0; i < output.results.length; i++) {    
        console.log("reading result: " + i);
            var row = ` <tr>
                                    <td> ${output.results[i].provider}</td>
                                    <td> ${output.results[i].name}</td>
                                    <td> ${output.results[i].pickup}</td>
                                    <td> ${output.results[i].arrival}</td>
                                    <td> ${output.results[i].price}</td>
                                    <td> ${output.results[i].seats}</td>
                                    <td> ${output.results[i].shared}</td>
                                </tr>`
        table.innerHTML += row
    }
}
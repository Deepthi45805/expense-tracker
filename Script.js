async function addExpense() {

    const category =
        document.getElementById("category").value;

    const amount =
        document.getElementById("amount").value;

    const date =
        document.getElementById("date").value;

    await fetch("/expenses", {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            category,
            amount,
            date
        })
    });

    loadExpenses();
}

async function loadExpenses(){

    const response =
        await fetch("/expenses");

    const data =
        await response.json();

    const list =
        document.getElementById("expenseList");

    list.innerHTML = "";

    data.forEach(expense => {

        const li =
            document.createElement("li");

        li.innerHTML =
            `${expense.category} -
             ₹${expense.amount}
             (${expense.date})`;

        list.appendChild(li);
    });
}

loadExpenses();

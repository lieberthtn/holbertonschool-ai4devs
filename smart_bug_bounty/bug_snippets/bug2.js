async function fetchData() {
    let data = "initial";
    // Səhv: await unudulub, data dərhal qaytarılır
    setTimeout(() => {
        data = "updated";
    }, 100);
    return data;
}

fetchData().then(console.log); // Gözlənilən: "updated"

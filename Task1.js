let catalogue = {"Product A": 20, "Product B": 40, "Product C": 50};
let wrappingFee = 0;

let quantiA = parseInt(prompt("Enter the quantity of A: "));
let isWrappedA = prompt("Is this product wrapped as a gift (y/n): ");

if (isWrappedA === 'y') {
    wrappingFee = quantiA;
}

let quantiB = parseInt(prompt("Enter the quantity of B: "));
let isWrappedB = prompt("Is this product wrapped as a gift (y/n): ");

if (isWrappedB === 'y') {
    wrappingFee += quantiB;
}

let quantiC = parseInt(prompt("Enter the quantity of C: "));
let isWrappedC = prompt("Is this product wrapped as a gift (y/n): ");

if (isWrappedC === 'y') {
    wrappingFee += quantiC;
}

let subTotal = (quantiA * catalogue["Product A"]) + (quantiB * catalogue["Product B"]) + (quantiC * catalogue["Product C"]);

console.log("-----------------------BILL-----------------------");

for (let key in catalogue) {
    let quantity = 0;

    if (key === "Product A") {
        quantity = quantiA;
    } else if (key === "Product B") {
        quantity = quantiB;
    } else if (key === "Product C") {
        quantity = quantiC;
    }

    console.log("Product Name: ", key);
    console.log("Product Quantity: ", quantity);
    console.log("Total Amount of ", key, ": ", quantity * catalogue[key], "\n");
}

console.log("--------------------------------------------------");

console.log("Subtotal: ", subTotal);

function flat10Discount(subTotal) {
    return subTotal > 200 ? subTotal - 10 : subTotal;
}

function bulk5Discount(quantiA, quantiB, quantiC) {
    let priceA = quantiA * catalogue["Product A"];
    let priceB = quantiB * catalogue["Product B"];
    let priceC = quantiC * catalogue["Product C"];

    if (quantiA > 10) priceA *= 0.95;
    if (quantiB > 10) priceB *= 0.95;
    if (quantiC > 10) priceC *= 0.95;

    return priceA + priceB + priceC;
}

function bulk10Discount(quantiA, quantiB, quantiC, subTotal) {
    return (quantiA + quantiB + quantiC) > 20 ? subTotal * 0.9 : subTotal;
}

function tiered50Discount(quantiA, quantiB, quantiC) {
    let total = 0;
    let discounted = 0;

    if ((quantiA + quantiB + quantiC) > 30) {
        if (quantiA > 15) {
            total = (15 * catalogue["Product A"]) + ((quantiA - 15) * catalogue["Product A"] * 0.5);
            discounted = 1;
        }

        if (quantiB > 15 && (!total || total > (15 * catalogue["Product B"]) + ((quantiB - 15) * catalogue["Product B"] * 0.5))) {
            total = (15 * catalogue["Product B"]) + ((quantiB - 15) * catalogue["Product B"] * 0.5);
            discounted = 2;
        }

        if (quantiC > 15 && (!total || total > (15 * catalogue["Product C"]) + ((quantiC - 15) * catalogue["Product C"] * 0.5))) {
            total = (15 * catalogue["Product C"]) + ((quantiC - 15) * catalogue["Product C"] * 0.5);
            discounted = 3;
        }

        if (discounted === 1) {
            total += (quantiB * catalogue["Product B"]) + (quantiC * catalogue["Product C"]);
        } else if (discounted === 2) {
            total += (quantiA * catalogue["Product A"]) + (quantiC * catalogue["Product C"]);
        } else if (discounted === 3) {
            total += (quantiA * catalogue["Product A"]) + (quantiB * catalogue["Product B"]);
        }
    }

    return total;
}

let discount = flat10Discount(subTotal);
let discountName = "flat_10_discount";

let bulk5 = bulk5Discount(quantiA, quantiB, quantiC);

if (discount > bulk5) {
    discount = bulk5;
    discountName = "bulk_5_discount";
}

let bulk10 = bulk10Discount(quantiA, quantiB, quantiC, subTotal);

if (discount > bulk10) {
    discount = bulk10;
    discountName = "bulk_10_discount";
}

let tiered50 = tiered50Discount(quantiA, quantiB, quantiC);

if (discount > tiered50 && tiered50 !== 0) {
    discount = tiered50;
    discountName = "tiered_50_discount";
}

console.log("Discount Name: ", discountName);
console.log("Discount Amount: ", subTotal - discount);

let shippingFee = 0;
let totalQuantity = quantiA + quantiB + quantiC;

if (totalQuantity % 10 !== 0) {
    shippingFee = Math.floor(totalQuantity / 10) * 5 + 5;
} else {
    shippingFee = Math.floor(totalQuantity / 10) * 5;
}

console.log("Shipping Fee: ", shippingFee);
console.log("Wrapping Fee: ", wrappingFee);

let total = discount + shippingFee + wrappingFee;
console.log("Total: ", total);

const ticketPrices = { Infant: 0, Child: 10, Adult: 20 };
const cart = [];

class ticketPurchaseError extends Error {}

class paymentError extends Error {}

class seatReservationError extends Error {}

function calcTotalPrice(numInfants, numChildren, numAdults) {
  /* calculates the total price for the requested tickets based on the number entered

    parameters:
    numInfants (int): The number of infants.
        numChildren (int): The number of children.
        numAdults (int): The number of adults.

        returns:
        float:  the total price for the requested tickets.
     */
  if (numAdults === 0) {
    console.log("there are no adults to buy tickets");
    throw new ticketPurchaseError("no adults to purchase tickets");
  }

  if (numInfants > numAdults) {
    console.log("the number of infants can't exceed the number of adults");
    throw new ticketPurchaseError(
      "Number of infants cannot exceed the number of adults"
    );
  }
  if (numInfants + numChildren + numAdults > 20) {
    console.log("cannot purchase more than 20 tickets at once.");
    throw new ticketPurchaseError(
      "cannot purchase more than 20 tickets at once"
    );
  }
  let totalPrice = 0;
  totalPrice += numChildren * ticketPrices["Child"];
  totalPrice += numAdults * ticketPrices["Adult"];
  return totalPrice;
}

function makePayment(totalPrice) {
  /* Makes a payment request to the `TicketPaymentService` for the given total price.

    Args:
        totalPrice (float): The total price for the tickets.

    Raises:
        PaymentError: If the payment could not be completed successfully.
    */

  let paymentSuccess = true;
  if (!paymentSuccess) {
    throw new paymentError("Payment could not be completed");
  }
}

function makeseatReservation(numInfants, numChildren, numAdults) {
  /*
    Makes a seat reservation request to the `SeatReservationService` for the given number of infants, children and adults.

   parameters :
        numInfants (int): The number of infants.
        numChildren (int): The number of children.
        numAdults (int): The number of adults.

    Raises:
        SeatReservationError: If the seat reservation could not be completed successfully.
    */
  let SeatReservationSuccess = true;
  if (!SeatReservationSuccess) {
    throw new seatReservationError("Seat reservation could not be completed");
  }
}

function addItemTocart(numInfants, numChildren, numAdults) {
  try {
    const totalPrice = calcTotalPrice(numInfants, numChildren, numAdults);
    const item = { numInfants, numChildren, numAdults };
    cart.push(item);
    console.log(`Added item to cart: ${JSON.stringify(item)}`);
  } catch (error) {
    console.error(`Failed to add item to cart: ${error.message}`);
  }
}

async function checkout() {
  function askToContinue() {
    const response = prompt("Do you want to continue shopping?").toUpperCase();
    if (response === "Y") {
      return "continue";
    } else if (response === "N") {
      return "exit";
    } else {
      console.error("Invalid input. please enter Y or N");
      return askToContinue();
    }
  }

  let shopping = true;
  while (shopping) {
    try {
      let numInfants = parseInt(prompt("Enter the number of infants:"));
      let numChildren = parseInt(prompt("Enter the number of children:"));
      let numAdults = parseInt(prompt("Enter the number of adults:"));

      const totalPrice = calcTotalPrice(numInfants, numChildren, numAdults);
      console.log(`Total price: £${totalPrice}`);

      const confirmation = prompt(
        "Would you like to add these items to your cart? (Y/N)"
      );
      if (confirmation && confirmation.toUpperCase() === "Y") {
        addItemTocart(numInfants, numChildren, numAdults);
      }

      const paymentConfirmation = prompt(
        "Would you like to make a payment for the items in your cart? (Y/N)"
      );
      if (paymentConfirmation.toUpperCase() === "Y") {
        makePayment(totalPrice);
        console.log("Payment successful!");
      } else {
        console.log("Payment cancelled");
      }

      const reservationConfirmation = prompt(
        "Would you like to make a seat reservation for the items in your cart? (Y/N)"
      );
      if (reservationConfirmation.toUpperCase() === "Y") {
        makeseatReservation(numInfants, numChildren, numAdults);
        console.log("Seat reservation successful!");
      } else {
        console.log("Seat reservation cancelled");
      }

      const continueShopping = askToContinue();
      if (continueShopping === "exit") {
        shopping = false;
      } else {
        console.log(`Current cart: ${JSON.stringify(cart)}`);
      }
    } catch (error) {
      console.log(`Failed to checkout: ${error.message}`);
      if (error instanceof ticketPurchaseError) {
        console.log("Please try again with valid ticket purchase details");
        numInfants = NaN;
        numChildren = NaN;
        numAdults = NaN;
      } else if (error instanceof paymentError) {
        console.log("Please try again with a valid payment method");
      } else if (error instanceof seatReservationError) {
        console.log("Please try again with valid seat details");
      } else {
        console.log("Please try again with valid details");
      }
    }
  }
}

checkout();

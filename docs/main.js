// Global State variables
let numberOfNights = 1;
let cart = []; // Array containing booked items [{id, name, checkIn, checkOut, nights, pricePerNight, totalPrice}]
let checkInPicker, checkOutPicker;

// SafeStorage
const SafeStorage = {
    getItem: function (key) {
        try {
            return localStorage.getItem(key);
        } catch (e) {
            return null;
        }
    },
    setItem: function (key, value) {
        localStorage.setItem(key, value);

    },
    removeItem: function (key) {
        localStorage.removeItem(key);
    }
};
localStorage.clear();
// Load cart safely from SafeStorage if exists
const storedCart = SafeStorage.getItem('pyhotel_cart');
if (storedCart) {
    try {
        cart = JSON.parse(storedCart);
    } catch (e) {
        cart = [];
    }
}

// DOM Elements
const checkInEl = document.getElementById('check-in-date');
const checkOutEl = document.getElementById('check-out-date');
const daysIndicator = document.getElementById('days-count-indicator'); //  გასასწორებელია
const dateRangeReadable = document.getElementById('date-range-readable');
const consoleRoomSelect = document.getElementById('console-room-select');
const consolePricingSummary = document.getElementById('console-pricing-summary');

const toastEl = document.getElementById('toast');
const toastMessageEl = document.getElementById('toast-message');
const cartBadge = document.getElementById('cart-badge');
const cartContainer = document.getElementById('cart-items-container');
const cartTotalPriceEl = document.getElementById('cart-total-price');
const cartCheckoutBtn = document.getElementById('cart-checkout-btn');

// Set default dates 
const today = new Date();
const tomorrow = new Date(today);
tomorrow.setDate(tomorrow.getDate() + 1);

// Bootstrapping page load, custom Date setup
document.addEventListener("DOMContentLoaded", function () {


 
    checkInPicker = new Datepicker(checkInEl, {
        language: 'ka',
        minDate: today
    });

    checkInPicker.setDate(today);
    checkInEl.addEventListener('changeDate', function (e) {
        handleDateChange();
    })

    checkOutPicker = new Datepicker(checkOutEl, {
        language: 'ka',
        minDate: tomorrow
    });

    checkOutPicker.setDate(tomorrow);
    checkOutEl.addEventListener('changeDate', function (e) {
        handleDateChange();
    })

    handleDateChange();
    // updateCartUI();
});

// Custom function to safely show notifications via luxury Toast
function triggerToast(message) {
    toastMessageEl.textContent = message;
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastEl, { delay: 4500 });
    toastBootstrap.show();
}

// Handle  calendar check-in and check-out calculations
function handleDateChange() {

    const checkIn = checkInPicker.getDate();
    const checkOut = checkOutPicker.getDate();

    // თარიღების სიზუსტის შემოწმება
    if (checkIn && checkOut && checkOut > checkIn) {
        const diffTime = Math.abs(checkOut - checkIn);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        numberOfNights = diffDays;
        daysIndicator.textContent = numberOfNights;

        // Format readable Georgian date summary
        const options = { month: 'long', day: 'numeric' };
        const formattedIn = checkIn.toLocaleDateString('ka-GE', options);
        const formattedOut = checkOut.toLocaleDateString('ka-GE', options);
        dateRangeReadable.innerHTML = `<i class="fa-solid fa-circle-check text-success me-1"></i> ჯავშნის პერიოდი: <b>${formattedIn} - ${formattedOut}</b>`;
    } else {
        numberOfNights = 1;
        daysIndicator.textContent = '1';
        dateRangeReadable.innerHTML = `<i class="fa-solid fa-triangle-exclamation text-warning me-1"></i> გთხოვთ მიუთითოთ კორექტული თარიღები.`;
    }

    calculateConsolePricing();
}

// Update the pricing label on the main booking console button
function calculateConsolePricing() {
    const selectedOption = consoleRoomSelect.options[consoleRoomSelect.selectedIndex];
    const pricePerNight = parseFloat(selectedOption.getAttribute('data-price')) || 120;
    const total = pricePerNight * numberOfNights;
    consolePricingSummary.textContent = `${numberOfNights} ღამე • ${total} ₾`;
}

function handleRoomChange() {
    calculateConsolePricing();
}

// Select and scroll to booking console from Room List
function selectAndBook(roomName) {
    consoleRoomSelect.value = roomName;
    calculateConsolePricing();

    // Instant booking 
    bookFromConsole();

    // Scroll dynamically to booking card console
    document.querySelector('.booking-console-card').scrollIntoView({ behavior: 'smooth' });

    // Pulse the booking card to draw attention
    const consoleCard = document.querySelector('.booking-console-card');
    consoleCard.style.outline = "3px solid #f59e0b";
    setTimeout(() => {
        consoleCard.style.outline = "none";
    }, 1000);
}

// Booking 
function bookFromConsole() {
    const checkInVal = checkInEl.value;
    const checkOutVal = checkOutEl.value;
    const selectedRoomName = consoleRoomSelect.value;


    const selectedOption = consoleRoomSelect.options[consoleRoomSelect.selectedIndex];
    const pricePerNight = parseFloat(selectedOption.getAttribute('data-price')) || 120;

    if (!checkInVal || !checkOutVal) {
        return;
    }

    const totalPrice = pricePerNight * numberOfNights;
    const bookingId = 'ID-' + Math.floor(10000 + Math.random() * 90000);

    // Booking Object
    const newBooking = {
        id: bookingId,
        name: selectedRoomName,
        checkIn: checkInVal,
        checkOut: checkOutVal,
        nights: numberOfNights,
        pricePerNight: pricePerNight,
        totalPrice: totalPrice,
        paid: false
    };

    // მარჯვენა მოდალი
    const offcanvasEl = document.getElementById('cartOffcanvas');
    let bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl);
    if (!bsOffcanvas) {
        bsOffcanvas = new bootstrap.Offcanvas(offcanvasEl);
    }
    bsOffcanvas.show();

    cart.push(newBooking);
    SafeStorage.setItem('pyhotel_cart', JSON.stringify(cart));
    updateCartUI();
}

// წაშლა
function removeBooking(id) {
    cart = cart.filter(item => item.id !== id);
    SafeStorage.setItem('pyhotel_cart', JSON.stringify(cart));
    updateCartUI();
}


// განახლებული updateCartUI
function updateCartUI(showOnlyPaid = false) {
    cartContainer.innerHTML = '';
    const filteredCart = cart.filter(item => (showOnlyPaid ? item.paid : !item.paid));
    let totalCartSum = 0;

    // ღილაკის დამალვა/ჩვენება
    const checkoutBtn = document.getElementById('cart-checkout-btn');
    checkoutBtn.style.display = showOnlyPaid ? 'none' : 'block';

    if (filteredCart.length === 0) {
        cartContainer.innerHTML = `<div class="text-center py-5 text-secondary">ჯავშნები ცარიელია</div>`;
    } else {
        filteredCart.forEach(item => {
            totalCartSum += item.totalPrice;
            const itemCard = document.createElement('div');
            itemCard.className = 'card bg-white border border-light shadow-sm rounded-4 p-3 mb-3';
            itemCard.innerHTML = `
                <div class="d-flex justify-content-between">
                    <div>
                        <h6 class="fw-bold mb-1">${item.name}</h6>
                        <small class="text-muted">${item.checkIn} - ${item.checkOut}</small>
                    </div>
                    ${!item.paid ? `<button onclick="removeBooking('${item.id}')" class="btn btn-sm text-danger"><i class="fa-solid fa-trash"></i></button>` : ''}
                </div>
                <div class="mt-2 fw-bold">${item.totalPrice} ₾</div>
            `;
            cartContainer.appendChild(itemCard);
        });
    }
    cartTotalPriceEl.textContent = `${totalCartSum} ₾`;
    updateBadge(); // ბეჯის განახლება
}

// განახლებული checkoutAll - მოდალის მონაცემებით
function checkoutAll() {
    const pendingBookings = cart.filter(item => !item.paid);
    if (pendingBookings.length === 0) return;

    let sum = 0;
    pendingBookings.forEach(item => {
        item.paid = true;
        sum += item.totalPrice;
    });

    SafeStorage.setItem('pyhotel_cart', JSON.stringify(cart));

    // მოდალის მონაცემების შევსება
    document.getElementById('modal-booking-count').textContent = pendingBookings.length;
    document.getElementById('modal-booking-sum').textContent = `${sum} ₾`;

    const offcanvasEl = document.getElementById('cartOffcanvas');
    const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl);
    if (bsOffcanvas) bsOffcanvas.hide();

    const successModal = new bootstrap.Modal(document.getElementById('checkoutSuccessModal'));
    successModal.show();

    updateCartUI(false);
}

// ბეჯის ლოგიკა
function updateBadge() {
    const pendingItems = cart.filter(item => item.paid);
    cartBadge.textContent = pendingItems.length;
    cartBadge.classList.toggle('d-none', pendingItems.length === 0);
}


// გადახდილი ჯავშნები 
function showPaid() {
    updateCartUI(true);
    // თუ გსურთ ღილაკის დამატება უკან დასაბრუნებლად:
    cartContainer.insertAdjacentHTML('afterbegin', `
        <button onclick="updateCartUI(false)" class="btn btn-sm btn-outline-secondary mb-3 w-100">
            <i class="fa-solid fa-arrow-left"></i> უკან, გადასახდელებზე
        </button>
    `);
}
// მინი სქროლი
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('header');
    if (window.scrollY > 50) {
        navbar.classList.add('py-1', 'shadow-lg');
        navbar.classList.remove('py-2');
    } else {
        navbar.classList.add('py-2');
        navbar.classList.remove('py-1', 'shadow-lg');
    }
});
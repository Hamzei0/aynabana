jQuery('.gallery-slider').owlCarousel({
    loop: false,
    nav: false,
    dots: false,
    rtl: true,
    margin: 10,
    autoplay: false,
    autoplayTimeout: 5000,
    autoplayHoverPause: true,
    responsiveClass: true,
    responsive: {
        0: {
            items: 5,
        },

    }
});

jQuery(function () {

    jQuery(".accordion-button").on("click", function () {
        jQuery(".accordion-button").css("opacity", "0.6");
        jQuery(this).css("opacity", "1");
    });

});

jQuery(function () {
    jQuery(".thumb").on("click", function () {

        jQuery(".thumb").removeClass("active");
        jQuery(this).addClass("active");

        let newImage = jQuery(this).data("image");

        jQuery(".main-image img")
            .fadeOut(150, function () {
                jQuery(this)
                    .attr("src", newImage)
                    .fadeIn(150);
            });

    });


});
// jQuery(function () {

//     jQuery(".size-btn").on("click", function () {

//         jQuery(".size-btn").removeClass("active");
//         jQuery(this).addClass("active");

//         let price = jQuery(this).data("price");
//         let formattedPrice = price.toLocaleString("fa-IR");

//         jQuery(".product-price").text(formattedPrice + " تومان");

//     });

// });
// jQuery(".size-btn").on("click", function () {
//     jQuery(".current-size").text(jQuery(this).data("size"));
// });

jQuery(function () {

    function updateTotal() {
        let total = 0;

        jQuery(".cart-item").each(function () {
            let price = parseInt(
                jQuery(this).find(".item-price").data("price")
            );

            let qty = parseInt(
                jQuery(this).find(".cart-qty").val()
            );

            total += price * qty;
        });

        jQuery(".total-price").text(
            total.toLocaleString("fa-IR") + " تومان"
        );
    }

    // Quantity change
    jQuery(".cart-qty").on("input", function () {
        updateTotal();
    });

    // Remove item
    jQuery(".remove-item").on("click", function () {
        jQuery(this).closest(".cart-item").fadeOut(300, function () {
            jQuery(this).remove();
            updateTotal();
        });
    });

    updateTotal();

});

jQuery(function () {

    let discount = 0;

    const coupons = {
        "MIRROR10": 10,
        "MIRROR20": 20
    };

    function calculateTotal() {
        let total = 0;

        jQuery(".cart-item").each(function () {
            let price = parseInt(
                jQuery(this).find(".item-price").data("price")
            );

            let qty = parseInt(
                jQuery(this).find(".cart-qty").val()
            );

            total += price * qty;
        });

        let finalTotal = total;

        if (discount > 0) {
            finalTotal = total - (total * discount / 100);
        }

        jQuery(".total-price").text(
            finalTotal.toLocaleString("fa-IR") + " تومان"
        );
    }

    // Quantity change
    jQuery(".cart-qty").on("input", function () {
        calculateTotal();
    });

    // Remove item
    jQuery(".remove-item").on("click", function () {
        jQuery(this).closest(".cart-item").fadeOut(300, function () {
            jQuery(this).remove();
            calculateTotal();
        });
    });

    // Apply coupon
    jQuery(".coupon-btn").on("click", function () {
        let code = jQuery(".coupon-input").val().trim().toUpperCase();

        if (coupons[code]) {
            discount = coupons[code];

            jQuery(".coupon-message")
                .text(`کد تخفیف ${discount}% اعمال شد`)
                .css("color", "#50e3c2");

            calculateTotal();
        } else {
            discount = 0;

            jQuery(".coupon-message")
                .text("کد تخفیف نامعتبر است")
                .css("color", "#ff6b6b");

            calculateTotal();
        }
    });

    calculateTotal();

});



jQuery(function () {

    jQuery("#contact-form").on("submit", function (e) {
        e.preventDefault();

        jQuery(".contact-message")
            .text("پیام شما با موفقیت ارسال شد ✅")
            .css("color", "#50e3c2");

        // Reset form
        jQuery(this)[0].reset();
    });

});

jQuery(function () {

    jQuery(".filter-btn").on("click", function () {

        jQuery(".filter-btn").removeClass("active");
        jQuery(this).addClass("active");

        let filter = jQuery(this).data("filter");

        if (filter === "all") {
            jQuery(".portfolio-item").fadeIn();
        } else {
            jQuery(".portfolio-item").hide();
            jQuery("." + filter).fadeIn();
        }

    });

});

jQuery(function () {

    jQuery("#consultation-form").on("submit", function (e) {
        e.preventDefault();

        jQuery(".form-message")
            .text("درخواست شما با موفقیت ثبت شد ✅ به‌زودی با شما تماس می‌گیریم.")
            .css("color", "#50e3c2");

        this.reset();
    });

});

// loign

jQuery(function () {

    jQuery(".auth-tab").on("click", function () {

        jQuery(".auth-tab").removeClass("active");
        jQuery(this).addClass("active");

        jQuery(".auth-form").addClass("d-none");

        if (jQuery(this).data("target") === "login") {
            jQuery(".login-form").removeClass("d-none");
        } else {
            jQuery(".signup-form").removeClass("d-none");
        }
    });

    jQuery("#login-form").on("submit", function (e) {
        e.preventDefault();
        alert("ورود با موفقیت انجام شد ");
    });

    jQuery("#signup-form").on("submit", function (e) {
        e.preventDefault();
        alert("ثبت‌نام با موفقیت انجام شد ");
    });

});

// account

jQuery(function () {

    jQuery(".user-menu .nav-link").on("click", function () {

        jQuery(".user-menu .nav-link").removeClass("active");
        jQuery(this).addClass("active");

        let target = jQuery(this).data("target");

        if (!target) return;

        jQuery(".user-content").addClass("d-none");
        jQuery("#" + target).removeClass("d-none");
    });

});


$(".view-order").on("click", function () {
    let row = jQuery(this).closest("tr");
    let orderNumber = row.find("td:eq(0)").text();
    let product = row.find("td:eq(2)").text();
    let qty = row.find("td:eq(3)").text();
    let price = row.find("td:eq(4)").text();
    let status = row.find("td:eq(5)").text();


    let modalHtml = `
    <div class="modal fade" id="orderModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content glass-card p-4">
          <div class="modal-header">
            <h5 class="modal-title">جزئیات سفارش ${orderNumber}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <p>محصول: ${product}</p>
            <p>تعداد: ${qty}</p>
            <p>قیمت کل: ${price}</p>
            <p>وضعیت: ${status}</p>
          </div>
        </div>
      </div>
    </div>
    `;

    jQuery("body").append(modalHtml);
    jQuery("#orderModal").modal("show");

    jQuery("#orderModal").on("hidden.bs.modal", function () {
        jQuery(this).remove();
    });
});

// comment

jQuery(function () {

    // ارسال کامنت اصلی
    jQuery("#newCommentForm").on("submit", function (e) {
        e.preventDefault();

        let name = jQuery(this).find("input[type=text]").val();
        let email = jQuery(this).find("input[type=email]").val();
        let message = jQuery(this).find("textarea").val();

        let newComment = `
        <div class="comment mb-4">
            <div class="d-flex align-items-center mb-2">
                <div class="comment-avatar me-3">👤</div>
                <div>
                    <h6 class="mb-0 fw-bold">${name}</h6>
                    <small class="opacity-75">اکنون</small>
                </div>
            </div>
            <p class="mb-0 opacity-75">${message}</p>
            <button class="btn btn-sm btn-glass mt-2 reply-btn">پاسخ</button>
            <div class="replies mt-3 ms-5"></div>
        </div>
        `;

        jQuery(".comments-list").append(newComment);

        // پاک کردن فرم
        this.reset();
    });

    // پاسخ به کامنت‌ها (delegation برای کامنت‌های داینامیک)
    jQuery(".comments-list").on("click", ".reply-btn", function () {
        // اگر فرم پاسخ وجود دارد، حذف شود
        jQuery(this).siblings(".reply-form").remove();

        let replyForm = `
        <form class="reply-form mt-2">
            <input type="text" class="form-control glass-input mb-2" placeholder="نام شما" required>
            <textarea class="form-control glass-input mb-2" rows="2" placeholder="نظر شما" required></textarea>
            <button type="submit" class="btn btn-sm btn-glass">ارسال پاسخ</button>
        </form>
        `;
        jQuery(this).after(replyForm);
    });

    // ارسال پاسخ
    jQuery(".comments-list").on("submit", ".reply-form", function (e) {
        e.preventDefault();

        let name = jQuery(this).find("input[type=text]").val();
        let message = jQuery(this).find("textarea").val();

        let newReply = `
        <div class="comment mb-3">
            <div class="d-flex align-items-center mb-1">
                <div class="comment-avatar me-2">👤</div>
                <div>
                    <h6 class="mb-0 fw-bold">${name}</h6>
                    <small class="opacity-75">اکنون</small>
                </div>
            </div>
            <p class="mb-0 opacity-75">${message}</p>
        </div>
        `;

        jQuery(this).siblings(".replies").append(newReply);

        // حذف فرم بعد از ارسال
        jQuery(this).remove();
    });

});



// bottom of the codes 
var map = L.map('map').setView([35.713443, 51.501739], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; قدرت گرفته از سایت  <a href="#"> zintara </a> '
}).addTo(map);

L.marker([35.713443, 51.501739]).addTo(map)
    .bindPopup(' کابینت')
    .openPopup();
//You clicked the map at LatLng(35.713443, 51.501739)
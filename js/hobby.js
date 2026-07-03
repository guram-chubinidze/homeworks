 const textElement = document.getElementById("typing-text");

        // 1. ვიღებთ ორიგინალ ტექსტს და ვასუფთავებთ ტეგებისგან (რომ უსაფრთხოდ დაიბეჭდოს)
        let rawText = textElement.innerHTML;
        rawText = rawText.replace(/</g, "&lt;").replace(/>/g, "&gt;");

        const tempDiv = document.createElement("div");
        tempDiv.innerHTML = rawText;
        const fullText = tempDiv.textContent;

        textElement.innerHTML = ""; // ვასუფთავებთ საწყის კონტენტს
        let index = 0;

        function typeWriter() {
            if (index <= fullText.length) {
                // ხილული ტექსტი (რაც უკვე დაიბეჭდა)
                const visiblePart = fullText.slice(0, index);
                // უხილავი ტექსტი (რაც დარჩა, ინარჩუნებს ადგილს ეკრანზე, რომ სიტყვები არ გადახტეს)
                const hiddenPart = fullText.slice(index);

                // ვსვამთ ორ განსხვავებულ span-ში
                textElement.innerHTML = `
            <span class="visible-code">${visiblePart}</span><span class="hidden-code">${hiddenPart}</span>
        `;

                index++;
                textElement.classList.add("typing-active");
                setTimeout(typeWriter, 20); // ბეჭდვის სიჩქარე (80ms ძალიან გლუვია)
            } else {
                // ბეჭდვის დასრულებისას ვტოვებთ მხოლოდ სუფთა ტექსტს
                textElement.textContent = fullText;
                textElement.classList.remove("typing-active");
            }
        }

        // იწყებს ბეჭდვას 1 წამში
        setTimeout(typeWriter, 3000);
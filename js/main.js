document.addEventListener("DOMContentLoaded", () => {

    let globalCssLines = 399 // საერთო სტილები
    let globalJsLines = 68 // საერთო ჯს
    // 1. მთლიანი დოკუმენტის HTML ტექსტის აღება და ხაზებად დაჭრა
    const fullHTML = document.documentElement.outerHTML;
    const totalLines = fullHTML.split('\n').length;
    let globalTotalLines = totalLines+globalCssLines+globalJsLines // საერთო რაოდენობა

    // 2. ყველა <style> ბლოკის ხაზების დათვლა            
    let cssLines = 0;
    const styleTags = document.querySelectorAll('style');
    styleTags.forEach(tag => {
        cssLines += tag.textContent.split('\n').length;
    });

    // 3. ყველა <script> ბლოკის ხაზების დათვლა
    let jsLines = 0;
    const scriptTags = document.querySelectorAll('script');
    scriptTags.forEach(tag => {
        jsLines += tag.textContent.split('\n').length;
    });

    // 4. HTML ხაზების გამოთვლა (საერთო ხაზებს გამოკლებული CSS და JS)
    // უზრუნველყოფს, რომ უარყოფითი ციფრი არ მივიღოთ დამრგვალებისას
    let htmlLines = Math.max(0, totalLines - (cssLines + jsLines));

    // 5. პროცენტების გამოთვლა
    const htmlPercent = Math.round((htmlLines / globalTotalLines) * 100) || 0;
    const cssPercent = Math.round(((cssLines + globalCssLines) / globalTotalLines) * 100) || 0;
    const jsPercent = Math.round(((jsLines + globalJsLines) / globalTotalLines) * 100) || 0;

    // მონაცემთა მასივი ვიზუალიზაციისთვის (ფერები GitHub-ის მიხედვით)
    const metricsData = [
        { name: "HTML", percentage: htmlPercent, color: "#e34c26" },
        { name: "CSS", percentage: cssPercent, color: "#563d7c" },
        { name: "JavaScript", percentage: jsPercent, color: "#f1e05a" }
    ];

    // სორტირება პროცენტების მიხედვით (დიდიდან პატარისკენ, როგორც სურათზეა)
    metricsData.sort((a, b) => b.percentage - a.percentage);

    // 6. DOM-ში ბარების გენერირება
    const container = document.getElementById("fileMetricsContainer");
    container.innerHTML = ""; // გასუფთავება

    metricsData.forEach(item => {
        const langItem = document.createElement("div");
        langItem.classList.add("lang-item"); // CSS სტილები აიღე წინა პასუხიდან

        langItem.innerHTML = `
      <div class="lang-info" style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px; color: #acbac7;">
        <span class="lang-name">${item.name}</span>
        <span class="lang-percentage">${item.percentage}%</span>
      </div>
      <div class="progress-bar-bg" style="width: 100%; height: 4px; background-color: #21262d; border-radius: 2px; overflow: hidden;">
        <div class="progress-bar-fill" style="height: 100%; width: 0%; background-color: ${item.color}; border-radius: 2px; transition: width 1s ease-in-out;"></div>
      </div>
    `;

        container.appendChild(langItem);

        // გლუვი შევსების ანიმაცია
        setTimeout(() => {
            langItem.querySelector(".progress-bar-fill").style.width = `${item.percentage}%`;
        }, 100);
    });
});
async function generateStory() {
    const theme = document.getElementById('theme').value;
    const setting = document.getElementById('setting').value;
    const plot = document.getElementById('plot').value;
    const characters = document.getElementById('characters').value;
    const length = document.getElementById('length').value;

    // Validate inputs
    if (!setting || !plot || !characters) {
        alert('Please fill in all fields');
        return;
    }

    // Show loading state
    const storyText = document.getElementById('story-text');
    storyText.innerHTML = '<p class="loading">Generating your story...</p>';

    try {
        const response = await fetch('/generate-story', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                theme,
                setting,
                plot,
                characters,
                length
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            storyText.innerHTML = `<p class="error">Error: ${data.error}</p>`;
            return;
        }

        if (data.story) {
            // Split by paragraphs and format properly
            const formattedStory = data.story.trim().split('\n').filter(p => p.trim()).map(paragraph =>
                `<p>${paragraph.trim()}</p>`
            ).join('');
            storyText.innerHTML = formattedStory;
        } else {
            storyText.innerHTML = '<p class="error">No story was generated. Please try again.</p>';
        }

    } catch (error) {
        storyText.innerHTML = '<p class="error">Error generating story. Please try again.</p>';
        console.error('Error:', error);
    }
} 
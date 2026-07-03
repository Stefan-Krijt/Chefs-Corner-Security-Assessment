// Calculate the secret recipe ID using SHA256
const serverSeed = 'default-seed-for-dev';
const recipeName = 'SECRETSAUCE';
const combined = serverSeed + ':' + recipeName;
async function calculateSha256(text) {
const encoder = new TextEncoder();
const data = encoder.encode(text);
const hashBuffer = await crypto.subtle.digest('SHA-256', data);
const hashArray = Array.from(new Uint8Array(hashBuffer));
const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
return hashHex;
}
calculateSha256(combined).then(hashHex => {
const recipeId = hashHex.substring(0, 16);
console.log('Combined string:', combined);
console.log('Full SHA256 hash:', hashHex);
console.log('Recipe ID (first 16 chars):', recipeId);
});
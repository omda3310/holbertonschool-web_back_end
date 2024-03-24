export default function getListStudentIds(users) {
    if (Array.isArray(users)) return users.map((user) => user.id);
    return [];
}

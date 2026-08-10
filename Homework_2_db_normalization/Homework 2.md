# Homework 2

---

# Part 1: Выбор сценария
Для данной работы был выбран сценарий: **Продажа билетов на мероприятия**. Эта система будет управлять площадками, мероприятиями, посетителями и купленными билетами.

---

# Part 2: Проектирование базы данных и документация

## Идентификация сущностей и атрибутов:

1. Площадки (Venues)
2. Мероприятия (Events)
3. Посетители (Visitors)
4. Билеты (Tickets)

---

## Проектирование таблиц:

---

# 1. Table Name: Venues
*   **Description**: Хранит информацию о площадках.
*   **Attributes**:
    *   `VenueId`: INTEGER, PK, NOT NULL, UNIQUE
    *   `Name`: VARCHAR(100), NOT NULL
    *   `Address`: VARCHAR(150), NOT NULL
    *   `City`: VARCHAR(60), NOT NULL
    *   `Capacity`: INTEGER, NOT NULL
*   **Constraints**:
    *   `PK_Venues`: PRIMARY KEY (VenueId)
    *   `UQ_FullAdress`: UNIQUE (Address, City)
    *   `CHK_Capacity`: CHECK (Capacity > 0)

---

# 2. Table Name: Events
*   **Description**: Хранит информацию о мероприятиях, проводимых на площадках.
*   **Attributes**:
    *   `EventId`: INTEGER, PK, NOT NULL, UNIQUE
    *   `VenueId`: INTEGER, FK (REFERENCES Venues), NOT NULL
    *   `Title`: VARCHAR(150), NOT NULL
    *   `EventDate`: DATE, NOT NULL
    *   `StartTime`: TIME, NOT NULL
    *   `EndTime`: TIME, NOT NULL
*   **Constraints**:
    *   `PK_Events`: PRIMARY KEY (EventId)
    *   `FK_Events_Venues`: FOREIGN KEY (VenueId) REFERENCES Venues(VenueId)
    *   `UQ_VenueSchedule`: UNIQUE (VenueId, EventDate, StartTime)
    *   `CHK_Times`: CHECK (StartTime < EndTime)

---

# 3. Table Name: Visitors
*   **Description**: Хранит информацию о посетителях.
*   **Attributes**:
    *   `VisitorId`: INTEGER, PK, NOT NULL, UNIQUE
    *   `FirstName`: VARCHAR(100), NOT NULL
    *   `LastName`: VARCHAR(100), NOT NULL
    *   `Email`: VARCHAR(255), NOT NULL, UNIQUE
*   **Constraints**:
    *   `PK_Visitors`: PRIMARY KEY (VisitorId)
    *   `UQ_Email`: UNIQUE (Email)
    *   `CHK_Email`: CHECK (Email LIKE ‘%@%’) – проверка, чтобы почта содержала символ @.

---

# 4. Table Name: Tickets
*   **Description**: Связывающая таблица, реализующая связь «многие-ко-многим» между таблицами Events и Visitors. Записывает информацию о проданных билетах.
*   **Attributes**:
    *   `TicketId`: INTEGER, PK, NOT NULL, UNIQUE
    *   `EventId`: INTEGER, FK (REFERENCES Events), NOT NULL
    *   `VisitorId`: INTEGER, FK (REFERENCES Visitors), NOT NULL
    *   `SeatNumber`: VARCHAR(10), NOT NULL
    *   `Price`: DECIMAL(6, 2), NOT NULL
    *   `Status`: VARCHAR(15), NOT NULL
*   **Constraints**:
    *   `PK_Tickets`: PRIMARY KEY (TicketId)
    *   `FK_Tickets_Events`: FOREIGN KEY (EventId) REFERENCES Events(EventId)
    *   `FK_Tickets_Visitors`: FOREIGN KEY (VisitorId) REFERENCES Visitors(VisitorId)
    *   `UQ_Tickets_Seat`: UNIQUE (EventID, SeatNumber)
    *   `CHK_Status`: CHECK (Status IN ('booked', 'paid', 'refunded'))

---

# Взаимосвязи:
*   **Venues и Events (Один-ко-Многим)**: одна площадка может проводить множество мероприятий, но каждое мероприятие проводится на одной площадке.
    *   `Events.VenueID` является внешним ключом, ссылающимся на `Venues.VenueID`.
*   **Events и Tickets (Один-ко-Многим)**: на одно мероприятие может быть продано множество билетов, но каждый билет относится к одному мероприятию.
    *   `Tickets.EventID` является внешним ключом, ссылающимся на `Events.EventID`.
*   **Visitors и Tickets (Один-ко-Многим)**: один посетитель может приобрести множество билетов, но каждый билет принадлежит одному посетителю.
    *   `Tickets.VisitorID` является внешним ключом, ссылающимся на `Visitors.VisitorID`.М
---


## Part 3: ER-диаграмма

![ER-диаграмма](er_diagram.png)

**Рисунок 1 – ER-диаграмма спроектированной базы данных**
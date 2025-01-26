import React from "react";
import styles from "./Request.module.css"; // Import the CSS module

const ComponentList = () => {
  const components = [
    { title: "Educational Qualifications", buttons: ["Edit", "Delete"] },
    { title: "Completed Projects", buttons: ["View", "Edit"] },
    { title: "Certifications", buttons: ["Download", "Share"] },
    { title: "LinkedIn and GitHub Profiles", buttons: ["Link", "Unlink"] },
    { title: "Ongoing Projects", buttons: ["Start", "Pause"] },
    { title: "Past Experience", buttons: ["View", "Edit"] },
  ];

  return (
    <div className={styles.componentList}>
        <h1 className={styles.heading}>Requests</h1>
      {components.map((component, index) => (
        <>
          <div key={index} className={styles.card}>
            <h2 className={styles.cardTitle}>{component.title}</h2>
            <div className={styles.buttonsWrapper}>
              {component.buttons.map((buttonText, btnIndex) => (
                <button key={btnIndex} className={styles.button}>
                  {buttonText}
                </button>
              ))}
            </div>
            <hr className={styles.divider} />
          </div>
        </>
      ))}
    </div>
  );
};

export default ComponentList;

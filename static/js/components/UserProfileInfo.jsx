import React from "react";
import { useSelector } from "react-redux";

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";

import UserAvatar from "./UserAvatar";

const UserProfileInfo = () => {
  const profile = useSelector((state) => state.profile);

  return (
    <Card>
      <CardContent>
        <div
          style={{
            display: "flex",
            justifyContent: "flex-start",
            flexDirection: "row",
            alignItems: "center",
          }}
        >
          <UserAvatar
            size={128}
            firstName={profile.first_name}
            lastName={profile.last_name}
            username={profile.username}
            gravatarUrl={profile.gravatar_url}
          />
          &nbsp;&nbsp;
          <h2
            id="userRealname"
            style={{
              visibility: !(profile.first_name || profile.last_name)
                ? "hidden"
                : "visible",
            }}
          >
            {profile.first_name} {profile.last_name}
          </h2>
        </div>
        &nbsp;
        <br />
        <Typography component="div">
          <Box pb={1}>
            <Box fontWeight="fontWeightBold" component="span" mr={1}>
              User roles:
            </Box>
            {profile.roles.join(", ")}
          </Box>
          {profile.acls?.length && (
            <Box pb={1}>
              <Box fontWeight="fontWeightBold" component="span" mr={1}>
                Additional user ACLs (separate from role-level ACLs):
              </Box>
              {profile.acls.join(", ")}
            </Box>
          )}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default UserProfileInfo;
